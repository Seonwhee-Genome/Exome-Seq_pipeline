class GS_AnnoVar_operation(object):

    def __init__(self):
        self.anno_cmd = "perl /data1/home/tools/annovar/"
        self.hg19_db = "/data1/home/tools/annovar/humandb/"

    def vcf_conversion(self, vcf_path, out_path):
        Command = self.anno_cmd + "convert2annovar.pl %s -format vcf4 -allsample -withfreq > %s" %(vcf_path, out_path)
        self.execution_annoVar(Command)

    def get_SIFT_score(self, annovar_file):
        Command = self.anno_cmd + "annotate_variation.pl -buildver hg19 -filter -dbtype avsift %s %s " %(annovar_file, self.hg19_db)
        self.execution_annoVar(Command)

    def annotating_variants(self, input_file):
        Command = self.anno_cmd + "annotate_variation.pl -buildver hg19 %s %s" % (input_file, self.hg19_db)
        self.execution_annoVar(Command)


    def execution_annoVar(self, cmd):
        print("Your command is %s" % (cmd))
        sp.call(cmd, shell=True)
