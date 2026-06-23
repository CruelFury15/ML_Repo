import os
import warnings
from pathlib import Path
from statistics import multimode

os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")
warnings.filterwarnings(
    "ignore",
    message="Could not find the number of physical cores.*",
    category=UserWarning,
    module="joblib.externals.loky.backend.context",
)

try:
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import datasets
    from sklearn.cluster import KMeans
except ModuleNotFoundError as error:
    missing_package = error.name
    raise SystemExit(
        "Missing required package: "
        f"{missing_package}. Install the project dependencies with "
        "`pip install numpy matplotlib scipy scikit-learn` and run this script again."
    ) from error


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_digits_overview(digits):
    fig = plt.figure(figsize=(6, 6))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    for index in range(64):
        axis = fig.add_subplot(8, 8, index + 1, xticks=[], yticks=[])
        axis.imshow(digits.images[index], cmap=plt.cm.binary, interpolation="nearest")
        axis.text(0, 7, str(digits.target[index]))

    fig.savefig(OUTPUT_DIR / "digits_overview.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


def save_sample_digit(digits, index=100):
    fig, axis = plt.subplots(figsize=(3, 3))
    axis.imshow(digits.images[index], cmap=plt.cm.gray_r, interpolation="nearest")
    axis.set_title(f"Target: {digits.target[index]}")
    axis.axis("off")
    fig.savefig(OUTPUT_DIR / "sample_digit.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


def build_cluster_mapping(labels, targets, cluster_count):
    mapping = {}

    for cluster_index in range(cluster_count):
        mask = labels == cluster_index
        if np.any(mask):
            mapping[cluster_index] = int(multimode(targets[mask].tolist())[0])

    return mapping


def save_cluster_centers(model, mapping):
    fig = plt.figure(figsize=(8, 3))
    fig.suptitle("Cluster Center Images", fontsize=14, fontweight="bold")

    for index, center in enumerate(model.cluster_centers_):
        axis = fig.add_subplot(2, 5, index + 1)
        axis.imshow(center.reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest")
        axis.axis("off")
        axis.set_title(f"Cluster {index}: {mapping.get(index, '?')}")

    fig.savefig(OUTPUT_DIR / "cluster_centers.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


def write_report(description, shape_lines, mapping, predicted_clusters, predicted_digits):
    report_path = Path("index.html")
    mapping_rows = "\n".join(
        f"<tr><td>{cluster}</td><td>{digit}</td></tr>" for cluster, digit in sorted(mapping.items())
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Handwriting Recognition Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.5;
      margin: 2rem auto;
      max-width: 960px;
      padding: 0 1rem;
    }}
    img {{
      border: 1px solid #ddd;
      display: block;
      height: auto;
      margin: 1rem 0 2rem;
      max-width: 100%;
    }}
    table {{
      border-collapse: collapse;
      margin: 1rem 0 2rem;
      width: 100%;
    }}
    th,
    td {{
      border: 1px solid #ddd;
      padding: 0.5rem;
      text-align: left;
    }}
    th {{
      background: #f3f4f6;
    }}
    pre {{
      background: #f8fafc;
      overflow-x: auto;
      padding: 1rem;
    }}
  </style>
</head>
<body>
  <h1>Handwriting Recognition Report</h1>
  <p>{shape_lines}</p>
  <h2>Dataset Description</h2>
  <pre>{description}</pre>
  <h2>Sample Digit</h2>
  <img src="outputs/sample_digit.png" alt="Sample handwritten digit">
  <h2>First 64 Digits</h2>
  <img src="outputs/digits_overview.png" alt="First 64 handwritten digit samples">
  <h2>Cluster Mapping</h2>
  <table>
    <thead><tr><th>Cluster</th><th>Interpreted Digit</th></tr></thead>
    <tbody>
      {mapping_rows}
    </tbody>
  </table>
  <h2>Cluster Centers</h2>
  <img src="outputs/cluster_centers.png" alt="KMeans cluster centers">
  <h2>Prediction</h2>
  <p>Predicted cluster labels: {predicted_clusters.tolist()}</p>
  <p>Predicted digits: {''.join(str(digit) for digit in predicted_digits)}</p>
</body>
</html>
"""
    report_path.write_text(html, encoding="utf-8")


def main():
    digits = datasets.load_digits()
    print(digits.DESCR[:500])
    print("Checking data shape:", digits.data.shape)
    print("Checking target shape:", digits.target.shape)
    print("Target at index 100:", digits.target[100])

    save_sample_digit(digits)
    save_digits_overview(digits)

    cluster_count = 10
    model = KMeans(n_clusters=cluster_count, n_init=10, random_state=42)
    labels = model.fit_predict(digits.data)
    mapping = build_cluster_mapping(labels, digits.target, cluster_count)

    print("Cluster-to-digit mapping:", mapping)
    save_cluster_centers(model, mapping)

    new_samples = np.array(
        [
[0.00,0.00,1.91,1.78,0.00,0.00,0.00,0.00,0.00,2.02,8.23,8.32,7.98,5.21,0.22,0.00,0.10,7.01,7.22,3.25,4.92,8.31,4.04,0.00,1.38,8.32,3.05,0.00,0.00,5.86,7.19,0.00,2.20,8.32,1.69,0.00,0.00,5.21,7.35,0.00,3.30,8.32,0.49,0.00,0.08,6.95,5.82,0.00,3.33,8.32,2.04,1.66,4.52,8.32,2.46,0.00,1.65,7.96,8.32,8.32,8.32,5.37,0.00,0.00],
[0.00,0.11,1.58,3.11,3.12,0.33,0.00,0.00,5.70,8.17,8.32,8.32,8.32,7.19,0.90,0.00,8.32,4.68,2.58,0.85,1.73,7.92,5.57,0.00,8.32,1.16,0.00,0.00,0.00,5.15,7.45,0.00,8.14,6.38,0.93,0.00,0.05,6.60,6.65,0.00,2.58,7.90,8.20,5.89,6.42,8.32,3.13,0.00,0.00,0.67,4.24,7.06,6.77,3.55,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.04,3.92,6.92,7.94,7.97,4.80,0.00,0.00,3.60,8.32,6.06,4.19,5.73,8.30,1.63,0.00,4.95,7.56,0.00,0.00,0.60,8.32,3.33,0.00,4.66,7.91,0.15,0.00,0.68,8.32,3.33,0.00,2.76,8.32,5.81,5.47,7.15,8.24,1.44,0.00,0.29,5.17,6.65,6.66,6.04,2.44,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,1.21,1.43,0.04,0.00,0.23,4.40,5.22,6.73,8.32,8.32,4.91,0.00,3.82,8.32,7.31,8.20,3.69,5.64,7.91,0.00,5.78,6.41,0.01,0.53,0.00,5.32,7.19,0.00,5.83,7.12,1.12,0.00,0.63,7.94,4.55,0.00,2.40,7.80,7.97,6.66,7.86,8.10,1.26,0.00,0.00,0.94,4.79,5.46,4.78,1.84,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
]
    )

    predicted_clusters = model.predict(new_samples)
    predicted_digits = [mapping[label] for label in predicted_clusters]

    print("Predicted cluster labels:", predicted_clusters)
    print("Predicted digits:", "".join(str(digit) for digit in predicted_digits))

    shape_lines = f"Data shape: {digits.data.shape}. Target shape: {digits.target.shape}."
    write_report(
        digits.DESCR[:500],
        shape_lines,
        mapping,
        predicted_clusters,
        predicted_digits,
    )


if __name__ == "__main__":
    main()
