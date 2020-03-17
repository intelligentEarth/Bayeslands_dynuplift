#!/bin/bash
batch=$2

# dos2unix ${batch}_variables.csv

# for badlands_model_run in AUSLG002 AUSLG003 AUSLG001
# do
badlands_model_run=$1
ID=$3

echo "run is" ${badlands_model_run}
echo "batch is" ${batch}
echo "ID is" ${ID}


# Pulls parameters from specified model run, prints to new file
awk -F"," -v COLT=${badlands_model_run} '
        NR==1 {
                for (i=1; i<=NF; i++) {
                        if ($i==COLT) {
                              title=i;
                                print $i;
                      }
                }
        }
        NR>1 {
                if (i=title) {
                        print $i;
                }
        }
    ' ${batch}/${ID}/${batch}_variables.csv > ${batch}/${ID}/modelvariables_${badlands_model_run}.txt

while read variable; do
    variables+=($variable)
done < ${batch}/${ID}/modelvariables_${badlands_model_run}.txt

echo "FOUND FILE HERE ${batch}/${ID}/modelvariables_${badlands_model_run}"

echo ${variables[0]}

dt_model=${variables[4]}
resol=${variables[2]}
scale_factor=${variables[5]}

echo "dt_model is" ${dt_model}

./dt_change.sh ${badlands_model_run} ${dt_model} ${resol} ${scale_factor} ${batch} ${ID}

./${dt_model}_xml_generation.sh ${badlands_model_run} ${batch} ${ID}

echo "done generating input files for " ${badlands_model_run}

rm  ${batch}/${ID}/modelvariables_${badlands_model_run}.txt
