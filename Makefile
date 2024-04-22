.PHONY: git
git:
	git add . \
	&& git commit --message "$(if $(m),$(m),default commit)" \
	&& git push

.PHONY: serve
serve:
	mdbook serve --hostname 127.0.0.1 --port 3333 --open
