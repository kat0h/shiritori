cat "$1" | sed "s/《\S*?》|｜|［\S*?］//g" | mecab | grep "名詞" | sed "s/,/ /g" | awk -v 'OFS=,' '{print $1,$9}' | grep -v ',$' | sed "s/,/ /g" | LC_ALL=C sort -k2 | uniq | sed "s/ /,/g"
