## 如何开服务? 

首先解释一下为什么要开服务? 开了服务之后, 我们就可以远程访问了. 我们可以在任何地方, 使用这个工具. 

怎么开服务? 分以下几步. 

* 启动服务. 也就是跑`serving.py`代码. 也可以双击`StartServing.bat`这个文件开启. 这个是一个flask服务, 端口给它写死, 是54233 ("武术233"的谐音), ip地址是`localhost:54233` . 不过这个仅能在本机使用. 如果是将localhost转为ip地址, 那也只能在内网才能访问. 

* 启动nginx, 以实现外网访问. 利用nginx来监听开放的`80` 端口, 然后将访问这个端口的请求转到`54233`接口去. 首先需要在nginx的`conf/nginx.conf`文件里面去改东西, 如下. 然后在nginx.exe所在的文件夹下使用`start nginx`把nginx跑起来就好了. 至于更多开启以及关掉nginx服务的东西, 参见[这里](https://www.jianshu.com/p/865ae9869f48) ~~再双击运行nginx.exe把nginx服务给它跑起来就好啦~~.  

  ```nginx
  ......
  
  events {
      ......
  }
  
  http {
      
      ......
          
      server{
          listen 80; ## 监听访问80端口的请求...
          server_name heheda;
          location /{
              proxy_pass http://localhost:54233; ## ...给它转发到这里
              proxy_redirect off;
          }
      }
  
  }
  
  ```

* 利用任一机器, 访问这个机器的ip地址(不用标端口号了), 就能使用服务啦. 

  * `xxx.xxx.xxx.xxx/next` 访问这个页面, 就能得到一个武术的名字, 你就知道下一步应该练习什么武术了. 吼吼吼, 完事儿了. 