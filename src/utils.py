def Error(error: str, at_line=None) -> None:
    print(f"======== Error ========\n{error} at line {at_line}") if at_line else  print(f"======== Error ========\n{error}")
    exit(0)

