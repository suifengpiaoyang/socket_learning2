# socket_learning
Learning the socket connection

第一种方式：使用最常见的阻塞模式  
第二种方式：使用非阻塞模式来实现多客户端连接  
很多文章都说这么做浪费 CPU 资源，因为不断轮询再加上异常处理  
理论上有道理，但我没有实际测试系统资源消耗。不过有更好的方式  
可以使用  
