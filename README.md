## Home Page

- https://hainghia.github.io/
https://rust-lang.github.io/mdBook/format/configuration/renderers.html

## [mdBook is a command line tool to create books with Markdown](https://rust-lang.github.io/mdBook)

### [Installation](https://rust-lang.github.io/mdBook/guide/installation.html)

This will automatically download mdBook from crates.io, build it, and install it in Cargo's global binary directory (`~/.cargo/bin/` by default).

```shell
cargo install mdbook
cargo install --git https://github.com/rust-lang/mdBook.git mdbook

# Uninstall 
cargo uninstall mdbook
```

## [Command Line Tool](https://rust-lang.github.io/mdBook/cli/index.html)

### [The init command](https://rust-lang.github.io/mdBook/cli/init.html)

```shell
mdbook init .
```

### [The build command](https://rust-lang.github.io/mdBook/cli/build.html)

```shell
mdbook build
```

### [The watch command](https://rust-lang.github.io/mdBook/cli/watch.html)

```shell
mdbook watch
```

### [The serve command](https://rust-lang.github.io/mdBook/cli/serve.html)

```shell
mdbook serve --hostname 127.0.0.1 --port 3333 --open
```

### [The test command](https://rust-lang.github.io/mdBook/cli/test.html)

```shell
mdbook test
```

### [The clean command](https://rust-lang.github.io/mdBook/cli/clean.html)

```shell
mdbook clean
```