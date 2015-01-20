##!/usr/bin/python
from operator import mul

def scale(fac,list):
    return map(mul,len(list)*[fac],list)

# scenarios and samples
scenarios = ['MC','data']
#SAMPLES = ['WJets','TTbar','TTbar_DiLep','TTbar_SinLep','T1tttt_1500_100','T1tttt_1200_800','T1tttt_800_450','T1tttt_1300_100','T1qqqq_1400_15']
SAMPLES = ['WJets','TTbar','TTbar_DiLep','TTbar_SinLep','DYJets','QCD','SingleTop','TTH','TTW','TTZ','T1tttt_1500_100','T1tttt_1200_800','T5tttt_1000_280','T5tttt_1300_280','T5tttt_1000_285','T5tttt_1300_285','T1ttbbWW_1300_290','T1ttbbWW_1300_295','T1ttbbWW_1000_715','T1ttbbWW_1000_720','SqGl_1300_100']
treename = 'treeProducerSusySingleLepton/'
base = '/nfs/dust/cms/group/susy-desy/Run2/MC/CMGtuples/Phys14_v1/'
Lumi = 4 #given in fb^-1
Lumi = Lumi * 1000

# prepare empty dictionaries
dirsHT={}
inDir={}
xsec_lumi={}
evtgen={}
for scene in scenarios:
    inDir[scene]={}

##################################
#       BACKGROUNDS
##################################
sample = 'TTbar'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [809.1*Lumi] #cross section in pb
inDir['MC'][sample] = base+'TTJets'
##################################
sample = 'TTbar_SinLep'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [809.1*Lumi] #cross section in pb
inDir['MC'][sample] = base+'TTJets/'
##################################
sample = 'TTbar_DiLep'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [809.1*Lumi] #cross section in pb
inDir['MC'][sample] = base+'TTJets/'
##################################
sample = 'WJets'
dirsHT[sample]  = ['WJetsToLNu_HT100to200/','WJetsToLNu_HT200to400/','WJetsToLNu_HT400to600/','WJetsToLNu_HT600toInf/']
xsec_lumi[sample] = [1817.0*1.23,471.6*1.23,55.61*1.23,18.81*1.23]
xsec_lumi[sample] = scale(Lumi,xsec_lumi[sample])
inDir['MC'][sample] = base+'WJets/'

##################################
sample = 'QCD'
dirsHT[sample]  = ['QCD_HT_250To500/','QCD_HT_500To1000/','QCD_HT_1000ToInf/']
xsec_lumi[sample] = [670500,26740,769.7]
xsec_lumi[sample] = scale(Lumi,xsec_lumi[sample])
inDir['MC'][sample] = base+'QCD/'

##################################
sample = 'DYJets'
dirsHT[sample]  = ['DYJetsToLL_M50_HT100to200/','DYJetsToLL_M50_HT200to400/','DYJetsToLL_M50_HT400to600/','DYJetsToLL_M50_HT600toInf/']
xsec_lumi[sample] = [194.3*1.27,52.24*1.27,6.546*1.27,2.179*1.27]
xsec_lumi[sample] = scale(Lumi,xsec_lumi[sample])
inDir['MC'][sample] = base+'DYJets/'

##################################
sample = 'TTH'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [0.5085*Lumi]
inDir['MC'][sample] = base+'TTH/'
##################################
sample = 'TTW'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [0.6647*Lumi]
inDir['MC'][sample] = base+'TTWJets/'
##################################
sample = 'TTZ'
dirsHT[sample]  = ['/']
xsec_lumi[sample] = [0.8565*Lumi]
inDir['MC'][sample] = base+'TTZJets/'
################################## Not HT bins different top decay chains
sample = 'SingleTop'
dirsHT[sample]  = ['TToLeptons_tch/','TToLeptons_sch/','T_tWch/','TBarToLeptons_tch/','TBarToLeptons_sch/','TBar_tWch/']
xsec_lumi[sample] = [136.05*0.108*3,7.20*0.108*3,35.6,80.97*0.108*3,4.16*0.108*3,35.6]
xsec_lumi[sample] = scale(Lumi,xsec_lumi[sample])
inDir['MC'][sample] = base+'SingleTop/'
#       SIGNAL
##################################
sample = 'T1tttt_1500_100'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.0141903*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1500_mLSP100/'
##################################
sample = 'T1tttt_1200_800'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.085641*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1200_mLSP800/'
## DESY PRIVATE
sample = 'T1tttt_800_450'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [1.489*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl800_mLSP450/'
##################################
sample = 'T1tttt_1300_100'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1300_mLSP100/'
##################################
sample = 'T1qqqq_1400_15'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi] # FIXME
inDir['MC'][sample] = base+'SMS_Gl_Gl_mGl1400_mLSP300_mChi315/'
##################################
##################################
#       SIGNAL
##################################
sample = 'T1tttt_1500_100'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.0141903*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1500_mLSP100/'
##################################
sample = 'T1tttt_1200_800'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.085641*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1200_mLSP800/'
## DESY PRIVATE

sample = 'T5tttt_1300_280'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'T5ttttDeg_mGo1300_mStop300_mChi280/'

sample = 'T5tttt_1000_280'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.325388*Lumi]
inDir['MC'][sample] = base+'T5ttttDeg_mGo1000_mStop300_mChi280/'


sample = 'T5tttt_1300_285'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'T5ttttDeg_mGo1300_mStop300_mCh285_mChi280/'

sample = 'T5tttt_1000_285'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.325388*Lumi]
inDir['MC'][sample] = base+'T5ttttDeg_mGo1000_mStop300_mCh285_mChi280/'


sample = 'T1ttbbWW_1000_715'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.325388*Lumi]
inDir['MC'][sample] = base+'T1ttbbWW_mGo1000_mCh725_mChi715/'


sample = 'T1ttbbWW_1000_720'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.325388*Lumi]
inDir['MC'][sample] = base+'T1ttbbWW_mGo1000_mCh725_mChi720/'


sample = 'T1ttbbWW_1300_290'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'T1ttbbWW_mGo1300_mCh300_mChi290/'

sample = 'T1ttbbWW_1300_295'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'T1ttbbWW_mGo1300_mCh300_mChi295/'

sample = 'SqGl_1300_100'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.151*Lumi]
inDir['MC'][sample] = base+'Sq_Gl_4t_Gl1300_Sq1300_LSP100/Loop/'


'''
sample = 'T1tttt_800_450'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [1.489*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl800_mLSP450/'
##################################
sample = 'T1tttt_1300_100'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi]
inDir['MC'][sample] = base+'SMS_T1tttt_2J_mGl1300_mLSP100/'
##################################
sample = 'T1qqqq_1400_15'
dirsHT[sample] = ['/']
xsec_lumi[sample] = [0.044*Lumi] # FIXME
inDir['MC'][sample] = base+'SMS_Gl_Gl_mGl1400_mLSP300_mChi315/'
##################################
'''
