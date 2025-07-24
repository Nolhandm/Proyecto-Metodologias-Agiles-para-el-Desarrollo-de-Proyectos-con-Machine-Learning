import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load models
@st.cache_resource
def load_models():
    with open("../models/som_model.pkl", "rb") as f:
        som = pickle.load(f)
    kmeans = joblib.load("../models/kmeans_model.joblib")
    return som, kmeans

som, kmeans = load_models()

st.title("Clustering by Self-Organizing Map (SOM)")
st.write("Upload a CSV file with the same structure as training datas")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "Country Name" not in df.columns:
        st.error("⚠️ Column 'Country Name' is not present.")
    else:
        X = df.drop(columns=["Country Name"])

        # Predict with SOM model
        bmu_indices = np.array([som.winner(x) for x in X.to_numpy()])
        flat_indices = [pos[0] * som._weights.shape[1] + pos[1] for pos in bmu_indices]
        som_weights = som.get_weights().reshape(-1, X.shape[1])
        cluster_labels = kmeans.predict(som_weights)
        assigned_clusters = [cluster_labels[i] for i in flat_indices]

        df["SOM Cluster"] = assigned_clusters

        st.success("✅ Clustering done.")

        # Affichage du DataFrame
        st.subheader("Results :")
        st.dataframe(df[["Country Name", "SOM Cluster"]].sort_values("SOM Cluster"))

        # PCA
        st.subheader("PCA projection of clusters")
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)

        fig, ax = plt.subplots(figsize=(10, 6))
        for cluster_id in sorted(set(assigned_clusters)):
            idx = df["SOM Cluster"] == cluster_id
            ax.scatter(X_pca[idx, 0], X_pca[idx, 1], label=f"Cluster {cluster_id}")

        for i, name in enumerate(df["Country Name"]):
            ax.annotate(name, (X_pca[i, 0], X_pca[i, 1]), fontsize=7, alpha=0.6)

        ax.set_title("Clustering SOM (PCA projection)")
        ax.set_xlabel("PCA 1")
        ax.set_ylabel("PCA 2")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        print("ℹ️ To leave the app, use Ctrl+C in the terminal.")

        # Téléchargement
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download result in CSV",
            data=csv,
            file_name="resultats_som.csv",
            mime="text/csv",
        )

st.caption("ℹ️ To leave the app, use Ctrl+C in the terminal.")