# owoify
owoify your source code!

# Usage

Install requirements via `pip install -r requirements.txt`

Then run the program in the directory of your source code to owoify it via `python3 uwuify.py`.

Alternatively, if you wish to only edit a single file you can use the `--file` argument. E.g `python3 uwuify.py --file main.cpp`

This program will (attempt) to create a backup of source files, in case anything goes wrong.

# Compatibility

Currently, the program only works with .inc files. I have tested this program with the pokeemerald repository and it works fine.

It currently has issues with files that have `[]` in them, as it replaces text between them. I have attempted to fix this to no avail. For example:

```
char* abilities[3] =
{
  [ABILITY_FORECAST] = "FORECAST",
  ...
}
```
get changed to 
```
char* abilities[3] =
{
  [ABILITY_FWORECAST] = "FWORECAST",
  ...
}
```

# Contributing

You can help by fixing the following issues/bugs, or by implementing new features such as:

- Specifiying a specific directory instead of just a specific file
- Fixing the [] issue
- Testing and finding bugs with other languages
- excludeLines only fire in events for their language (e.g #include isn't checked in a java source file)
- Modularise it by adding a function for your specific language compatibility fix

If you fix a bug for a specific language, please make sure to add the source file extension to the fileExts list, make sure the fix uses a function and edit the readme to show it has compatibility with that language.

An example can be found in the source code, in the function `def editInc(line):`. 

# Screenshots
![Image of pokemon emerald. Will add alt text later](pokeemerald.png)
![Image of pokemon emerald owoified. Will add alt text later](pokeemerald_owo.png)
