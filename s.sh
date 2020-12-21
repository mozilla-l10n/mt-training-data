for file in *csv;do

mkdir "${file%.*}"
mv "$file" "sumo_$file"
mv "sumo_$file" "${file%.*}"
done
