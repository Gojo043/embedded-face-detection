# src/config.py

"""
Central configuration for the face recognition project.

To switch cameras, change CAMERA_INDEX:
  0 = built-in laptop camera
  1 = first external USB camera
  2 = second external USB camera

Run this script directly to find your camera index:
  python -m src.config
"""

# ── Change this to your external camera index ──────────────────────────────
CAMERA_INDEX: int = 1
# ───────────────────────────────────────────────────────────────────────────

MODEL_PATH: str = "models/embedder_arcface.onnx"
DB_NPZ_PATH: str = "data/db/face_db.npz"
DB_JSON_PATH: str = "data/db/face_db.json"
ENROLL_DIR: str = "data/enroll"


def find_cameras(max_check: int = 5) -> None:
    """Utility: print which camera indices are available on this machine."""
    import cv2

    print("Scanning for available cameras...")

    found = []

    for i in range(max_check):
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            print(f"  [index {i}] Camera FOUND")
            found.append(i)
            cap.release()
        else:
            print(f"  [index {i}] No camera")

    if found:
        print(f"\nSet CAMERA_INDEX to one of: {found}")
    else:
        print("\nNo cameras found. Check connections.")


if __name__ == "__main__":
    find_cameras()
