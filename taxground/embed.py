"""Embedders. The local stand-in is deterministic, so a run can be rebuilt from its recorded inputs."""
import numpy as np


class LocalEmbedder:
    """Stand-in for an approved embedding model: TF-IDF over words and word pairs, reduced with truncated SVD (LSA).
    Fitted on the run's own normalised corpus with a fixed seed, so it is reproducible bit for bit."""

    def __init__(self, corpus, dim=64, seed=7):
        from sklearn.decomposition import TruncatedSVD
        from sklearn.feature_extraction.text import TfidfVectorizer
        big = len(corpus) > 5000                    # real corpora: drop one-off terms, cap the vocabulary, more dimensions
        self.vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english",
                                   min_df=3 if big else 1, max_features=300000 if big else None,
                                   dtype=np.float32 if big else np.float64)
        dim = 128 if big else dim
        X = self.vec.fit_transform(corpus)
        self.dim = min(dim, X.shape[0] - 1, X.shape[1] - 1)
        self.svd = TruncatedSVD(n_components=self.dim, random_state=seed, algorithm="arpack").fit(X)
        self.name = f"local-lsa-{self.dim}"

    def encode(self, texts):
        Z = self.svd.transform(self.vec.transform(list(texts)))
        Z /= np.linalg.norm(Z, axis=1, keepdims=True) + 1e-12
        return np.round(Z, 6).astype(np.float32)


class SentenceTransformerEmbedder:
    """Production option: any sentence-transformers model inside the approved environment (DG-2)."""

    def __init__(self, model_name):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)
        self.name = model_name
        self.dim = self.model.get_sentence_embedding_dimension()

    def encode(self, texts):
        return np.asarray(self.model.encode(list(texts), normalize_embeddings=True), dtype=np.float32)
