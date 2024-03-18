.PHONY: git
git:
	git add . \
	&& git commit --message "$(if $(m),$(m),default commit)" \
	&& git push
