# Models Folder

Trained model files are saved here after running `train_model.py` or the Colab notebook.

- `salary_model.pkl` — Trained Random Forest Regressor
- `label_encoders.pkl` — LabelEncoders for categorical features

> These `.pkl` files are listed in `.gitignore` to avoid committing large binary files to GitHub.
> Run `python train_model.py` from the project root to regenerate them.
