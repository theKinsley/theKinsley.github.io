FILE=content/todo/$1.md
if ! [ -f "$FILE" ]; then
    hugo new todo/$1.md
fi
echo $2 >> $FILE
