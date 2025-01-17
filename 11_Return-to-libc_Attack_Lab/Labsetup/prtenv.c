void main()
{
    char *shell = getenv("MYSHELL");
    if (shell)
    {
        printf("  Address: %x\n", (unsigned int)shell);
    }
}