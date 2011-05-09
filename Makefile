SHELL=/bin/sh

MAIL_INGRESS=${DESTDIR}/var/lib/tactical-communication
PROJECT_FILES=Makefile communication.spec

get-tactical-ingress:
	@echo $@

install: get-tactical-ingress
	install -d ${MAIL_INGRESS}
	install mail-ingress/get-tactical-ingress ${MAIL_INGRESS}/get-tactical-ingress
	install mail-ingress/pm-get.rc ${MAIL_INGRESS}/.procmailrc

communication-1.0.tar.gz: ${PROJECT_FILES}
	tar --exclude-vcs -czf $@ .
