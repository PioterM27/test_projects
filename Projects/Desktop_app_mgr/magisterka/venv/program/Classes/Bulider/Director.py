from program.Classes.Bulider.Builder import Builder
from program.Classes.Bulider.Section import Section
class Director:
    _builder=None
    #_frame=Builder.getFrameCreate()
    #_entry=Builder.getEntryField()
    def setBuilder(self,builder):
        self._builder=builder
    def getSection(self):
        section=Section()

        frame=self._builder.getFrameCreate()
        section.setFrame(frame)

       # entry=self._builder.getEntryField()
        #section.setEntry(entry)

        return section
