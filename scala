flatmap
list(list(1,2),list(3,4))->flatmap->list(1,2,3,4)


scala
val 不可变
var 可变
synchronized 确保线程同步

StreamingContext 
三种状态 初始化，活动中，已终止


sparkContext.setCallSite(startSite.get)
sparkContext.clearJobGroup()
sparkContext.setLocalProperty(SparkContext.SPARK_JOB_INTERRUPT_ON_CANCEL, "false")
savedProperties.set(SerializationUtils.clone(sparkContext.localProperties.get()))
scheduler.start()
