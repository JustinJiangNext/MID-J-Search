if ! test -d ./MidjourneyCSV-Kaggle; then
    echo "Fetching CSV from git..."
    git clone https://github.com/JustinJiangNext/MidjourneyCSV-Kaggle
    echo "Unzipping package..."
    cd MidjourneyCSV-Kaggle
    python3 unzip.py
    echo "Finished"
else
    echo "Alreading downloaded and unzipped"
fi

