import sys
import os
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

CLASSES = ['cardboard', 'electronic', 'foodwaste', 'glass', 'metal', 'paper', 'plastic', 'textile']

def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluate_submission.py <path_to_submission.csv> [path_to_test_ground_truth.csv]")
        sys.exit(1)

    sub_path = sys.argv[1]
    gt_path = sys.argv[2] if len(sys.argv) >= 3 else os.path.join(os.path.dirname(__file__), "test_ground_truth.csv")

    df_sub = pd.read_csv(sub_path)
    df_gt = pd.read_csv(gt_path)

    df_sub["image_id"] = df_sub["image_id"].astype(str).str.replace(".jpg", "", regex=False).str.zfill(3)
    df_gt["image_id"] = df_gt["image_id"].astype(str).str.replace(".jpg", "", regex=False).str.zfill(3)

    df_gt_labeled = df_gt[df_gt["waste_category"].notna() & (df_gt["waste_category"].str.strip() != "")].copy()
    if len(df_gt_labeled) == 0:
        print("Error: test_ground_truth.csv belum memiliki label! Silakan labeli via index.html lalu download test_ground_truth.csv.")
        sys.exit(1)

    merged = pd.merge(df_gt_labeled, df_sub, on="image_id", suffixes=("_gt", "_pred"))
    y_true = merged["waste_category_gt"].str.strip().str.lower()
    y_pred = merged["waste_category_pred"].str.strip().str.lower()

    acc = accuracy_score(y_true, y_pred)
    print("=" * 65)
    print(f"HASIL EVALUASI LOKAL: {os.path.basename(sub_path)}")
    print("=" * 65)
    print(f"Total Test Ground Truth Terlabeli : {len(merged)} / 480")
    print(f"Jumlah Prediksi Cocok             : {(y_true == y_pred).sum()} / {len(merged)}")
    print(f"Jumlah Prediksi Berbeda           : {(y_true != y_pred).sum()}")
    print(f">>> ESTIMASI SKOR LEADERBOARD     : {acc:.4f} ({acc*100:.2f}%)")

    if "uncertain" in merged.columns:
        conf_mask = merged["uncertain"].astype(str).isin(["0", "False", "false", ""])
        if conf_mask.sum() > 0:
            acc_conf = accuracy_score(y_true[conf_mask], y_pred[conf_mask])
            print(f">>> AKURASI (TANPA GAMBAR RAGU)   : {acc_conf:.4f} ({acc_conf*100:.2f}% pada {conf_mask.sum()} gambar)")

    print("\n--- Classification Report per Kelas ---")
    print(classification_report(y_true, y_pred, labels=CLASSES, digits=4, zero_division=0))

    mismatches = merged[y_true != y_pred][["image_id", "waste_category_gt", "waste_category_pred"]]
    if len(mismatches) > 0:
        print(f"--- Daftar Gambar yang Berbeda ({len(mismatches)} gambar) ---")
        print(mismatches.to_string(index=False))

if __name__ == "__main__":
    main()
