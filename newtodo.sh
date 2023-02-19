FILE=content/todo/$1.md
if ! [ -f "$FILE" ]; then
    hugo new todo/$1.md
    #python posting.py $FILE

fi
echo
echo $2 >> $FILE
