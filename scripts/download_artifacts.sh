#!/usr/bin/bash

ROOT="$(dirname "$(dirname "$(readlink -fm "$0")")")"
ARTIFACTS_PATH="$ROOT/data/artifacts"
mkdir $ARTIFACTS_PATH
cd $ARTIFACTS_PATH

wget 'https://upload.wikimedia.org/wikipedia/commons/7/79/Reis_Arborio.JPG' -O arborio.jpg
wget 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbr0EeZYqua5gLGiEFnKulwDpoKYIyysYZ5Q&s' -O basmati.jpg

dvc add $ARTIFACTS_PATH
dvc push
