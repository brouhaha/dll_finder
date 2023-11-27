# dll_finder - Given one or more Windows executables, get paths of necessary DLLs

Copyright 2023 Eric Smith

dll_finder development is hosted at the
[dll_finder Github repository](https://github.com/brouhaha/dll_finder/).

## Introduction

dll_finder is used when cross-compiling Windows executables on Linux using
the MinGW suite. When packaging such executables, it is necessary to include
some DLLs provided by MinGW packages. dll_finder is used to obtain a list
of the necessary DLL paths.
