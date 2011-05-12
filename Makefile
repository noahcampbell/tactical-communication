SHELL=/bin/sh

VERSION=1.0
MAIL_INGRESS=${DESTDIR}/var/lib/tactical-communication
ATTACHMENT_DIR=${DESTDIR}/var/tactical/activity
ACTIVITY_DIR=${DESTDIR}/var/tactical/ingress/attachments
PROJECT_FILES=Makefile communication.spec

communication-${VERSION}.tar.gz: ${PROJECT_FILES}
	@mkdir -p build
	tar --exclude=build --exclude-vcs -czf build/$@ .

install: 
	install -d ${MAIL_INGRESS}
	install -d ${ATTACHMENT_DIR}
	install -d ${ACTIVITY_DIR} 
	install mail-ingress/get-tactical-ingress ${MAIL_INGRESS}/get-tactical-ingress
	install mail-ingress/pm-get.rc ${MAIL_INGRESS}/.procmailrc
	install attachments/publish-attachments ${MAIL_INGRESS}/publish-attachments

clean:
	@rm build/communication-${VERSION}.tar.gz
