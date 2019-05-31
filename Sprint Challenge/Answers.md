  **What, in your opinion, is an important part of code reviews? That is, what is**
  **something you pay attention to when you review code, and that you appreciate**
  **when others do the same for your code?**
  
  Code reviews are crucial for creating and maintaining readable code. We use the
  same principle we would for any creative endeavor: the recipient of your creation
  (in this case, another software developer) is not inside your head.
  - Use clear, constructive criticism. Instead of "your indents are wrong" use "on lines 
  X, Y, and Z, you use tabs instead of four spaces."
  - If something is unclear, make suggestions that could be helpful.
  - Ask good questions where possible. Instead of "what does this do?," use "I'm not sure 
    what this parameter is supposed to mean. Can you clarify or use a more descriptive label?"
  
  **We have an awful lot of computers here, and it gets pretty confusing with**
  **slightly different things running on all of them. How could containers help us**
  **improve this situation?**
  
  Docker containers allow for "reproducible builds"; that is, they allow you to run software in
  a way that's consistent regardless of the underlying hardware on which they're run. They do
  this by creating a virtual environment based on a set of parameters--the Dockerfile--and running
  whatever code you put in them. Docker containers can help in the initial stages to make sure things
  run smoothly in a predictable environment before you move on to testing in more idiosyncratic settings.
  As a bonus, Docker containers provide a layer of security, since they don't run directly in the underlying software environment. 
