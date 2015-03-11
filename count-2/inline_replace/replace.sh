for count in $(seq 1 10) ; do echo "foo" >> file-$count; echo $count Done; done; 
#for file in $(ls *file*) ; do vim -c "silent! s/foo/bar/g | wq" $file ; echo $file done; done;
