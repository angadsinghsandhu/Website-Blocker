# <ins> Website-Blocker <ins>

## <ins> Description </ins>
A python project that outputs that blocks websites periodically
on your windows machine by changing the ` hosts ` file

in my system the hosts file is located in ` C:/Windows/System32/drivers/etc/hosts `
please check to see if yours is the same. Or else if it is different
please change the ` fhand ` location specified on the **"7th"** line of the 
` Blocker.pyw ` file

this example blocks ` "facebook.com" `, please add your prefered url to 
the ` "websites ` array in the **"11th"** line of the 
` Blocker.pyw ` file 

To schedule this file to run on your pc periodically please add it via
your `'task scheduler'` application in windows, this links might guide you 
to schedule the `.pyw` file

[Schedule and MANUALLY run .pyw script in Task Scheduler on Windows](https://stackoverflow.com/questions/51541502/schedule-and-manually-run-pyw-script-in-task-scheduler-on-windows/51541652)

[Scheduling a task in windows10 using .pyw file](https://stackoverflow.com/questions/61321911/scheduling-a-task-in-windows10-using-pyw-file)


---

## Project Details
* <ins>Name</ins> :  WebSite Bolcker
* <ins>Category</ins> :  Python

---

### Packages Used ###
| name     | PyPi Links |
| -------- | ---------- |
| time     | *in-built* |
| datetime | *in-built* |