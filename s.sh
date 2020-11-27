for file in *csv;do

mkdir "${file%.*}"
mv "$file" "${file%.*}"
done
