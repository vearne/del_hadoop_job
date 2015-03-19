# 过滤待删除的任务
keyword=$1
if [ -z "$keyword" ] ; then
    echo "参数不能为空"
    echo "用法: bash kill_job.sh <keyword> " 
    exit 
fi
curl -O http://192.168.1.100:50030/jobtracker.jsp

python parse.py | grep $keyword |sort| tee job.tmp

echo "---------------- start kill -------------------"
# 执行删除动作
cat ./job.tmp |sort| while read LINE
do
    #echo $LINE
    job_id=`echo $LINE|awk -F " " '{print $1}'| tr -d ' '`
    echo "kill job -- ${job_id}" 
    hadoop job -kill "$job_id"
done
