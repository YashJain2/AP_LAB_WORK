import speedtest

test=speedtest.Speedtest()
download=test.download()
upload=tesst.upload()
print("Download Speed : {}\nUpload Speed : {}",download,upload)
