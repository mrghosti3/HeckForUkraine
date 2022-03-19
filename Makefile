OUTPUT=needs_updater.ocmod.zip

all: ${OUTPUT}

%.zip: upload install.xml
	@zip -r $@ $^

clean:
	rm ${OUTPUT}
