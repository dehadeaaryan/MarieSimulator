
# MarieSimulator

Simulator for MARIE (Machine Architecture that is Really Intuitive and Easy)

## Code Format

```Python
from marieSimulator import Marie, MarieReader as mr

marie = Marie(mr('trial')) # Trial is the file containing Marie instructions
marie.run()
marie.show()
```

## Trial File

```Text
Load X
Add One
Store X
Halt
X, HEX 0000
One, HEX 0001
```

### Supported Opcodes (Instructions)

1. Load X
2. Store X
3. Add X
4. Subt X
5. Input
6. Output
7. Halt
8. Skipcond X
9. Jump X
10. Clear
11. AddI X
12. JumpI X
13. LoadI X
14. StoreI X
15. JnS X
16. HEX X
