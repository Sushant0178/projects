echo "BUILD START"

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files, clear old static files before collecting new ones
python manage.py collectstatic --noinput --clear

echo "BUILD END"
