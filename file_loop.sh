
ID=$1
batch=AUS

mkdir ${batch}
mkdir ${batch}/${ID}

model=001
model=${batch}${model}

./badlands_input_files.sh ${model} ${batch} ${ID}
