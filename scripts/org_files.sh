# Do not use this script. Files have been already organized
#!/bin/bash
diretorio="../topo"
for arquivo in "$diretorio"/*; do
    if [ -f "$arquivo" ]; then
        nome_arquivo=$(basename "$arquivo")
        nome_sem_extensao="${nome_arquivo%.*}"
        mkdir -p "$diretorio/$nome_sem_extensao"
        mv "$arquivo" "$diretorio/$nome_sem_extensao/"
        echo "Arquivo '$nome_arquivo' movido para '$diretorio/$nome_sem_extensao/'"
    fi
done
