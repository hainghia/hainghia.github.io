[group('mdbook')]
[positional-arguments]
mdbook-build *options:
    #!/usr/bin/env zsh
    set -euo pipefail

    mdbook build "$@"

[group('mdbook')]
[positional-arguments]
mdbook-watch *options:
    #!/usr/bin/env zsh
    set -euo pipefail

    mdbook watch "$@"

[group('mdbook')]
[positional-arguments]
mdbook-serve *options:
    #!/usr/bin/env zsh
    set -euo pipefail
    mdbook serve --hostname 127.0.0.1 --port 3333 --open "$@"

[group('mdbook')]
[positional-arguments]
mdbook-init name:
    #!/usr/bin/env zsh
    set -euo pipefail
    mdbook init "{{name}}"


[group('mdbook')]
mdbook-clean:
    #!/usr/bin/env zsh
    set -euo pipefail
    mdbook clean