
curl https://gist.githubusercontent.com/sebiglesias/ea2faa92f4b25a79f811104584e91efb/raw/02378f041ae64d3d021031efeb1572cbddfc2fc7/test-web-server-log.txt
touch log.txt
ls | grep -w "log.txt" #verifica si existe log.txt

curl https://gist.githubusercontent.com/sebiglesias/ea2faa92f4b25a79f811104584e91efb/raw/02378f041ae64d3d021031efeb1572cbddfc2fc7/test-web-server-log.txt >> log.txt
cat log.txt | grep “ 200 “ >> ok.txt
cat log.txt | grep “ 500 “ >> error.txt



