## 如何开服务? 

首先解释一下为什么要开服务? 开了服务之后, 我们就可以远程访问了. 我们可以在任何地方, 使用这个工具. 

怎么开服务? 分以下几步. 

* 启动服务. 也就是跑`serving.py`代码. 也可以双击`StartServing.bat`这个文件开启. 这个是一个flask服务, 端口给它写死, 是54233 ("武术233"的谐音), ip地址是`localhost:54233` . 不过这个仅能在本机使用. 如果是将localhost转为ip地址, 那也只能在内网才能访问. 

* 启动nginx, 以实现外网访问. 利用nginx来监听`80`端口, 然后将访问这个端口的请求转到`localhost:54233`接口去. 首先需要在nginx的`conf/nginx.conf`文件里面去改东西, 如下. 然后在nginx.exe所在的文件夹下使用`start nginx`把nginx跑起来就好了. 至于更多开启以及关掉nginx服务的东西, 参见[这里](https://www.jianshu.com/p/865ae9869f48) 可以使用`nginx -s quit`.  

  ```nginx
  ......
  
  events {
      ......
  }
  
  http {
      
      ......
      
      server{
          listen 80; ## 监听从外网发来的访问80端口的请求...
          server_name wushu;
          location / {
              proxy_pass http://localhost:54233; ## ...给它转发到本地的这里
              proxy_redirect off; 
          }
      }
  
  }
  
  ```

* 利用任一机器, 访问这个机器的ip地址 + 相应端口号, 就能使用服务啦. 

  * ``xxx.xxx.xxx.xxx:80` 进入欢迎界面. 
  * `xxx.xxx.xxx.xxx/next` 访问这个页面, 就能得到一个武术的名字, 你就知道下一步应该练习什么武术了.  
  * `xxx.xxx.xxx.xxx/yongchun?p=<1到8>`访问这个页面, 可以看咏春拳木人桩的截图文件. 

## 2021年3月23日

美化了页面, 理论上无需手动输入url了, 只需各种点点点了. 

## 2021年4月14日

如果需要放到Ubuntu服务器上, 可以参考这个教程: https://cloud.tencent.com/developer/article/1661061 写的比较清楚. 