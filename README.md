### Descrição

Port scanner using Python.

Test your site replacing the existent data in the `main.py` file:
```
url = "totidiversidade.com.br"
port_range = [0, 100]
```

In the `port_scanner.py` file,  was created a function called `get_open_ports` that takes a `target` argument and a `port_range` argument. `target` can be a URL or IP address. `port_range` is a list of two numbers indicating the first and last numbers of the range of ports to check.
Here is the syntax:
```
get_open_ports(target, port_range, verbose=False)
```
Here are examples of how the function may be called:
```
get_open_ports("209.216.230.240", [440, 445])
get_open_ports("www.stackoverflow.com", [79, 82])
```

The function should return a list of open ports in the given range.

The `get_open_ports` function should also take an optional third argument of `True` to indicate "Verbose" mode. If this is set to true, the function shourd return a descriptive string instead of a list of ports.

Here is the format of the string that should be returned in verbose mode (text inside `{}` indicates the information that should appear):
```
Open ports for {URL} ({IP address})
PORT     SERVICE
{port}   {service name}
{port}   {service name}

