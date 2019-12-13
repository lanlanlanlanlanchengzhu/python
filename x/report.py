# -*- coding: utf-8 -*-

from __future__ import division

import json

import pandas

expect_same = '["zxHouseLoanCnt","zxMaxCreditAmt","zxRcy12MAcctMaxDelqPeriod","zxRcy12MCreCardMaxDelqPeriod","zxRcy24MAcctMaxDelqPeriod","zxRcy24MCreCardMaxDelqPeriod","zxRcy6MAvgUseCreditAmt","zxTotalCreditAmt","zxAccountNowAccuDelq2Cnt","zxAccountNowMaxPeriod","zxAccountNowTotalDelqAmt","zxCreCardAcctNowTotalDelqAmt","zxAccountCnt","zxBadBebtsBalance","zxBadBebtsCnt","zxCreCardAcctNowAccuDelq2Cnt","zxCreCardAcctNowMaxPeriod","zxCreCardMaxMonthsCnt","zxCreCardStatus1","zxCreCardStatus2","zxCreCardStatus3","zxCreCardStatus4","zxCreCardStatus5","zxCreditBal","zxCreditCardAccountCnt","zxCreditRetCode","zxFirstCreditCardMonth","zxFirstLoanMonth","zxHouseFundPayStatus","zxHouseLoanBalCnt2","zxLastQueryTime","zxLoanBalCnt2","zxMaxMonths","zxRcy12MClsAcctMaxDelqPeriod","zxRcy12MHouseAccuDelq1Cnt","zxRcy12MHouseAccuDelq2Cnt","zxRcy24MClsAcctMaxDelqPeriod","zxRcy3MAddCreCardAmt","zxRcy3MAddLoanAmt","zxRcy3MCreCardQueryCompanyCnt","zxRcy3MLoanQueryCompanyCnt","zxReportDate2","zxWarrantLoanType","zxBlanceShouldPayAmt","zxCreCardNowShouldPayAmt","zxCreCardUseCreditRate","zxCreCardUsedAmtSum","zxHouseFundCompanyRate","zxHouseFundMonthPayAmt","zxHouseFundPayLastMonth","zxHouseFundRecordUpdate","zxHouseFundSelfRate","zxHouseLoan1MAvgPayAmt","zxHouseLoanBal2","zxIssuBankCnt","zxOldUnClsCreCardMth","zxRcy12MCommerHouAccuDelq2Cnt","zxRcy12MOtherAccuDelq1Cnt","zxRcy12MOtherAccuDelq2Cnt","zxRcy24MCreCardAcctMaxRepayCnt","zxRcy3MAcctMaxDelqPeriod","zxRcy3MCreCardMaxDelqPeriod","zxRcy6MAcctMaxDelqPeriod","zxRcy6MCreCardMaxDelqPeriod","zxLoanRate","zxLoanRateMax","zxsAllLoanAcctBalanceList","zxsLoanAcctStatus","zxsLoanAmt","zxsLoanOrgName","zxsLoanPeriodsTotalNum","zxsLoanRepayMode","zxsLoanThisMonthActualRepayAmt","zxsLoanThisMonthRepayAmt","zxAccountNowAccuDelq2Cnt","zxAccountNowMaxPeriod","zxAccountNowTotalDelqAmt","zxCreCardAcctNowTotalDelqAmt","zxRcy12MAcctMaxDelqPeriod","zxRcy12MCreCardMaxDelqPeriod","zxFirstSemiCreditCardMonth","zxRcy1MCreCardQueryCompanyCnt","zxRcy1MLoanQueryCompanyCnt","zxRcy2MCreCardQueryCompanyCnt","zxRcy2MLoanQueryCompanyCnt","zxRestDisposalCnt","zxHouseFundMonthShouldPayAmt","zxMinCreditAmt","zxNmlCreCardSumUsedLmt","zx_credit_salary","zx_Mortgage_fac","zx_fac","zx_credit_sala","zx_risk_fac","zxRcy3MLoanQueryCnt","zxRcy3MCreCardQueryCnt","zxIsVcreditNull","zxHouseLoanAmt","zxLoanCnt","zxLoanBalCnt","zxResidenceStatus","zxJobTitle","zxPosition","zxLoanDelqStatus6To12Months","zxDegree","zxCareer","zxMaritalStatus","zxCompanyIndustry","zxHasG","zxHouseFundPayProv","zx1MthDelqMaxAmt","zxAccountForgCnt","zxAccountFtypeCnt","zxAccoutRepaymentRate","zxAcctCnt","zxAge","zxAge1","zxAllCreCardNowActualPayAmtList","zxAllCreCardNowShouldPayAmtList","zxAllCreCardNowStatusList","zxAllLoanAcctBalanceList","zxAllLoanAcctNowActualPayAmtList","zxAllLoanAcctNowShouldPayAmtList","zxAllLoanAcctRemainPaySumList","zxAutoLoanAmt","zxAverage2MaxSalaryRate","zxBalance2MaxSalaryRate","zxBlanceActualPayAmt","zxCarLoanBal2","zxClostAcctCnt","zxClsAcctCnt","zxCompanyStartYear","zxConsumeLoanBal","zxConsumeLoanBal2","zxCreCardAndAcctCnt","zxCreCardAverageSum","zxCreCardCreRate8AcctCnt","zxCreCardDelqM3OverAccoutCnt","zxCreCardDelqMaxAmt","zxCreCardLimitAvg","zxCreCardMaxDurationMth","zxCreCardMaxUseCreditRate","zxCreCardMaxUsed2TotalRate","zxCrecardMaxUsedAmt","zxCreCardMaxUsedAmtSum","zxCreCardMedianLmt","zxCreCardMinLmt","zxCreCardMinUseCreditRate","zxCreCardRepaymentRate","zxCreCardSecondLmt","zxCreCardUseCreditRate2","zxCreCardUsed2AverageRate","zxCreCardUsed2MaxRate","zxCreCardUsedLmt","zxCreditAvgLimit2","zxCreditAvgLimit3","zxCreditCardAccuDelqCnt","zxCreditCardAccuDelqCnt1","zxCreditCardDelqStatus30To60Days","zxCreditCardDelqStatus6To12Months","zxCreditCardRcyDelqDate","zxCurrDelqPeriodSum","zxCurrOverM1AmtSum","zxDelqM1OverAccoutCnt","zxDelqM1OverCnt","zxDelqMonths","zxEarliestWorkDuration","zxEarlyNmlCreCardMonths","zxEducation","zxHouseFundMaxRate","zxHouseFundMinRate","zxHouseFundUpdateTime","zxHouseLoanPeriod","zxIsHasGuaranteeInfo","zxIsHasGuasiCreditCardInfo","zxL12loanCreditAmountTotal","zxL12loanPrincipalAmountTotal","zxLoan1MApproved","zxLoanBalanceAmt","zxLoanBalTotalAmt","zxLoanBalTotalAmt2","zxLoanCompanyBalCnt","zxLoanCompanyBalCnt2","zxLoanDelqStatus30To60Days","zxLoanRcyDelqDate","zxLoanRcyUpdateDate","zxLoansCnt","zxMaxDays","zxMaxLoanAmt","zxMaxLoanBalanceAmt","zxMaxNmlCreCardYears","zxMaxSalary","zxMaxUpdated","zxMob12NeverDelqAccoutCnt","zxMob3NeverDelqAccoutCnt","zxMob6NeverDelqAccoutCnt","zxNmlCreCardAverageSum","zxNmlCreCardMaxLmt","zxNmlCreCardMaxUsedAmtSum","zxNmlCreCardSecondLmt","zxNmlCreCardUsed0AcctNum","zxNmlCreCardUsedAmt","zxNmlCreCardUsedLmt","zxNmlCreCardUsedRate","zxNmlCreditAvgLimit","zxNowNmlAcctLmtMax","zxNowNmlAcctMaxLmt","zxNowNmlLoanCnt","zxOldLoanMonths","zxOldLoanMth","zxOldUnClsCreCardLmt","zxOldUnClsCreCardMonths","zxOtherLoanBalCnt","zxPersonalLoanBalCnt2","zxPhone","zxRcy12MaxLoanAmt","zxRcy12MClsAcctMaxDelqAmt","zxRcy12MContsNotDelqPeriod","zxRcy12MCreCardNowAccuDelqCnt","zxRcy12MCreCardQueryCnt","zxRcy12MLoanQueryCnt","zxRcy12MLoanQueryCompanyCnt","zxRcy12MLoanUsedRate","zxRcy12MMaxLoanAmt","zxRcy12MTotalQuerCnt","zxRcy18LoanCnt","zxRcy1MSelfQuery","zxRcy24MBalAccoutAvgCreAmt","zxRcy24MCancelAcctMaxDelqAmt","zxRcy24MClsAcctMaxDelqAmt","zxRcy24MContsNotDelqPeriod","zxRcy24MCreCardCnt","zxRcy24MCreCardQueryCnt","zxRcy24MLoanQueryCnt","zxRcy24MMaxDuration","zxRcy24MRangeDuration","zxRcy2YearsLoanMangeSum","zxRcy3MAccountMaxDelq1Cnt","zxRcy3MCreCardAcctMaxDelq1Cnt","zxRcy3MCreditCardCancelCnt","zxRcy3MCreditCardNoActivityCnt","zxRcy3MTotalQuerCnt","zxRcy6MAccountCnt","zxRcy6MAddCreCardAccotCnt","zxRcy6MAvgPayAmt","zxRcy6MContsNotDelqPeriod","zxRcy6MCreCardQueryCnt","zxRcy6MCreCardQueryCompanyCnt","zxRcy6MLoanQueryCnt","zxRcy6MMaxDelqCnt","zxRcy6MMaxDelqPeriod","zxRcy9MCreCardAcctMaxRepayCnt","zxRcy9MonCreCardAcctMaxRepayCnt","zxRcyLoanQueryDay","zxRcyLoanQueryDays","zxRcyNmlCreCardLmt","zxRcyUnClsCreCardLmt","zxRevCreditBal","zxSemiCreditCardAccountCnt","zxSendDate","zxSex","zxSTAvgChgMth","zxSTAvgChgMthCreditPlat","zxUseCreditAmt","zxUsedCreditAmountRate","zxWorkChangeTimes","zxActivityCreditMaxCreditAmount","zxConsumeLoanBalCnt2","zxCreCardMaxLmt","zxCreCardNotactiveCnt","zxCreCardNowActualPayAmt","zxCreditAvgLimit","zxIsBadAccount","zxIssuBankCorporateCnt","zxLoan2MApproved","zxLoan3MApproved","zxLstCdtLmtCnt","zxLstCdtLmtTotal","zxNmlCreCardUsed0AcctCnt","zxNoActCreditCardAccountCnt","zxOtherLoanBalAmt","zxRcy12MAccountCnt","zxRcy18MLoanCnt","zxRcy1MLoanQueryCnt","zxRcy1MLoanQueryCnt1","zxRcy2MLoanQueryCnt","zxRcy3MAccountCnt","zxRcy6MLoanQueryCompanyCnt","zxResidChangeTimes","zxSTMaxChgAmt","zxAutoLoanDate","zxCreCardAverage2TotalRate","zxCreCardCurrencyCnt","zxCreCardDelqAccoutCnt","zxCreditCardBalAccountCnt","zxCreditCardFirstOpenDate","zxCreditCardRcyUpdateDate","zxDelqCnt","zxFirstCreCardDate","zxFirstLoanDate","zxHouseFundPayDate","zxHouseMortgageBalance","zxHouseMortgageRemainPaySum","zxLoanDelqStatus60To90Days","zxLoanDelqStatus90To180Days","zxMinSalary","zxNowNmlCreCardCnt","zxPersonalLoanCnt","zxRcy12MCreCardAcctMaxDelq2Cnt","zxRcy12MMaxDelqPeriod","zxRcy1MCreCardQueryCnt","zxRcy1MLoanApprovalSum","zxRcy1MTotalQuerCnt","zxRcy24MCreCardAcctMaxDelq4OverCnt","zxRcy24MCreditCardAccountCnt","zxRcy24MMaxDelqPeriod","zxRcy3MCreCardAcctMaxDelq2Cnt","zxRcy6MAccountMaxDelq1Cnt","zxRcy6MTotalQuerCnt","zxRcyQueryDate","zxSTPrepayCnt","zxAccountRepaymentDate","zxAutoLoanBalance","zxCreCardAcctNowAccuDelq1Cnt","zxCreCardInactCnt","zxCreditCardDelqStatus24Months","zxCreditCardDelqStatus24MonthsCreditPlat","zxCreditCardDelqStatus60To90Days","zxCreditCardDelqStatus90To180Days","zxCreditRepaymentDate","zxDelqM3OverCnt","zxexceptBusinesLoanNowTotalDelqAmt","zxHouseFundPayFirstMonth","zxIfQryAssure","zxIsCreditRepayment","zxIsHasQueryInfo","zxIsQryAssure","zxLoan3MDelqM01Cnt","zxLoanOverM1AmtSum","zxNormalCreditAmountTotal","zxNormalCreditAmountTotalToUsed","zxPersonalLoanBal","zxRcy12MAccountMaxDelq1Cnt","zxRcy12MAccountMaxDelq2Cnt","zxRcy12MAccountMaxDelq3Cnt","zxRcy12MAccountNowAccuDelqCnt","zxRcy12MCancelAcctMaxDelqAmt","zxRcy12MCreCardAcctMaxDelq1Cnt","zxRcy24MCreCardAcctMaxDelq1Cnt","zxRcy24MCreCardAcctMaxDelq2Cnt","zxRcy24MCreCardTotalDelqCnt","zxRcy24MCreditCardDelqAccountCnt","zxRcy2YearsGuarApproSum","zxRcy3MAddCreCardAccotCnt","zxRcy3MCreCardQueryNum","zxRcy3MDelqM01Cnt","zxRcy6MAccountMaxDelq3Cnt","zxRcy6MCreCardAcctMaxDelq1Cnt","zxsCreCardDate","zxsCreCardLmt","zxsCreCardShareLmt","zxsHouseFundMonthPayAmt","zxsLoanDate","zxsRcy1MLoanQueryCompanyCnt","zxsRcy1MQuerCnt","zxsSemiCrdCardAccuDelqCnt60Days","zxsSemiCrdCardSumMthMaxBal60Days","zxStPCreCardMaxUsedAmtSum","zxsUnclearedLoanLegalbodyNum","zxCarLoanBal","zxCreCardOverM1AmtSum","zxCreCardUseCreditRatePercent","zxCreditCardDelqStatus30Dayyues","zxCreditCnt","zxCurrCreCardOverdueAmt","zxHouseLoanDate","zxRcy12MAddCreCardAccotCnt","zxRcy12MCancelAcctMaxDelqPeriod","zxRcy24MAccountMaxDelq1Cnt","zxRcy24MBalAccoutCnt","zxRcy24MCancelAcctMaxDelqPeriod","zxRcy2MCreCardQueryCnt","zxRcy3MLoanQueryNum","zxRcy6MCreCardAcctMaxDelq2Cnt","zxRevCreditCnt","maxLoan24MContsNotDelqPeriod","zxCreditCardDelq1MonthsAccuTimes","zxHouseFund","zxWorkChangeFreqMth","maxCreditCard12MContsNotDelqPeriod","maxCreditCard24MContsNotDelqPeriod","maxLoan12MContsNotDelqPeriod","maxLoan6MContsNotDelqPeriod","shareAmtSum","validIntervalMon","zxAccountNowAccuDelq1Cnt","zxAccountTotalLoanCnt","zxAutoLoanPeriod","zxBusinesLoanNowTotalDelqAmt","zxCompanyName","zxCreCardBadAccoutCnt","zxCreCardDelq12MonthsAccuAmt","zxCreCardDelq12MonthsAccuPeriod","zxCreCardDelq24mOpen","zxCreCardDelq3MonthsAccuPeriod","zxCreCardDelq6MonthsAccuAmt","zxCreCardDelqAccoutCnt2","zxCreCardHistoryMaxDelqAmt","zxCreditCardDelq2MonthsAccuTimes","zxCreditCardDelq3MonthsAccuTimes","zxCreditCardDelq4MonthsAccuTimes","zxCreditCardDelq7To12MonthsAccuTimes","zxGender","zxHouseFundBalance","zxHouseFundMaxIntervalMth","zxHouseFundPayCity","zxHouseFundRemainPaySum","zxHouseLoanBal","zxIsBadCreCardAcct","zxIsCreCardFrozen","zxLoanDelq24MonthsAccuAmt","zxLoanDelq6MonthsAccuAmt","zxMob24NeverDelqAccoutCnt","zxNewCompany","zxPersonalLoanBal2","zxRcy6MCreCardAcctMaxDelq3Cnt","zxsCompanyIndustry","zxsCompanyStartYear","zxsHouseFundNo","zxsHouseFundPayLand","zxsHouseFundPayStatus","zxsHouseFundSelfRate","zxsJobTitle","zxsPosition","zxsResidenceInfoUpdateDate","zxsResidenceStatus","zxRcy3MCreCardAcctMaxDelq3Cnt","zxCredCard3MDelqM01Cnt","zxRcy3MCreCardAcctMaxDelq4OverCnt","zxRcy3MAccountMaxDelq3Cnt","zxRcy3MAccountMaxDelq4OverCnt","zxRcy3MAccountMaxDelq2Cnt","zxRcy6MSemiCreditCardAcctMaxDelq3Cnt","zxsUnclsCrdIssuBankNum","zxsObjectionCnt","zxsSemiCrdCardMthLenMax60Days","zxRcy12MSemiCreditCardAcctMaxDelq3Cnt","maxCreditCard6MContsNotDelqPeriod","zxRcy6MAccountMaxDelq2Cnt","zxRcy6MCreCardAcctMaxDelq4OverCnt","zxRcy6MSemiCreditCardAcctMaxDelq4OverCnt","zxRcy6MSemiCreditCardAcctMaxDelq1Cnt","zxRcy6MSemiCreditCardAcctMaxDelq2Cnt","zxsSemiCrdCardOverdraftCnt60Days","zxRcy6MAccountMaxDelq4OverCnt","zxRcy12MTransferAcctMaxDelqPeriod","zxAccountFtypeCntCreditPlat","zxRcy6MSemiCreditCardMaxDelqPeriod","zxRcy24MTransferAcctMaxDelqPeriod","zxBusinesLoan12MAcctMaxDelqPeriod","zxRcy24MSemiCreditCardAcctMaxDelq3Cnt","zxsRcy2YearsSpecialQuerySum","zxRcy1MCreditCardCancelCnt","zxGuaranteeCnt","zxRcy12MAccountMaxDelq4OverCnt","zxRcy12MCreCardAcctMaxDelq3Cnt","zxRcy12MSemiCreditCardAcctMaxDelq2Cnt","zxRcy12MCreCardAcctMaxDelq4OverCnt","zxRcy12MSemiCreditCardAcctMaxDelq1Cnt","zxRcy12MSemiCreditCardAcctMaxDelq4OverCnt","zxHouseLoanDelqCnt","zxRcy1MOrgCreditCardApprovalSum","zxsUnclsCrdAccountCnt","zxsRcy1MCreCardQueryCompanyCnt","validIntervalCarAndAccoutMon","zxRcy24MAccountMaxDelq2Cnt","zxRcy24MAccountMaxDelq4OverCnt","zxRcy24MCreCardAcctMaxDelq3Cnt","zxRcy24MSemiCreditCardAcctMaxDelq1Cnt","zxRcy24MAccountMaxDelq3Cnt","zxsRcy1MLoanQueryCnt","zxRcy24MSemiCreditCardAcctMaxDelq2Cnt","zxDelqM1OverHouseLoanCnt","zxRcy24MLoanMore2","zxRcy24MSemiCreditCardAcctMaxDelq4OverCnt","zxRcy24MSemiCreditCardMaxDelqPeriod","zxRcy24MSemiCreditCardAccountNowAccuDelqCnt","zxsLowInsureFamilyMonthIncome","zxsRcy1MCreCardQueryCnt","zxCommerHouseLoanCnt","zxCarLoanBalCnt2","infRcy3MLoanQueryNum","zxRcy6MCreditCardCancelCnt","zxRcy12MCommerHouAccuDelq1Cnt","houseAndCarLoanCnt","lst12MOverdueCntToShouldPayMaxRate","zxRcy12MCreditCardCancelCnt","zxBadAccoutCnt","infRcy3MCreCardQueryNum","zxsRcy2YearsGuarApproSum","zxDelqAccoutCnt2","zxWarrantLoanCnt","infMob24NeverDelqAccoutCnt","zxDelqM3OverAccoutCnt","infAccoutRepaymentRate","zxSTMaxChgMthCreditPlat","infCreCardRepaymentRate","infCreCardUseCreditRate","zxsUnclsCrdCreditTotalAmt","infMob6NeverDelqAccoutCnt","zxGuaranteeBal","infMob12NeverDelqAccoutCnt","zxRestDisposalBalaceAmt","zxFrzCreCardUsedLmt","zxStPCreCardUsedLmt","zxSTMaxChgMth","unsettledConsumerLoanCnt","infAccoutDelq24mTotalOpen","thisMonShouldPayAmtSum","zxRcy12MTransferAcctMaxDelqAmt","zxRcy24MAcctTotalDelqCnt","zxSemiCreCardUsedLmt","creditShouldPayAmtSum","zxRcy24MTransferAcctMaxDelqAmt","zxsUnclsCrdSigBankMaxLmt","zxsRcy2YearsLoanMangeSum","infMob3NeverDelqAccoutCnt","infCreCardDelq24mOpen","zxLoanDelqPeriodSum","lst6mCharCntCrdAndLoanTotal","zxHouseLoanBalance","zxsUnclsCrdRec6mAveOverdraftBla","zxCreCardDelqPeriodSum","zxCommerHouseLoanBlance","zxFrzCreCardMaxUsedAmtSum","zxActivityQuasiCreditMaxCreditAmount","zxsUnclsCrdOverdraftBla","zxsUnclsCrdSigBankMinLmt","zxFrzCreCardAverageSum","zxStPCreCardAverageSum","zxsAdminiPenaltyEffecDate","zxsRewardEffecDate","zxCarryRecordMaxRegisterDate","zxsGuartCompsLstCompsDate","zxsHouseFundPayDate","zxsGuartCompsLstRepayDate","zxsExecutesStartDate","zxsPracticeGetDate","zxsAssetDisposaLstRepayDate","zxCarryRecordCloseDate","zxsSemiCreCardRepaymentDate","isHas24RepayMonthCredit","zxIsCreCardBadDebt","zxIsSemiCreCardBadDebt","zxIsHasLoanGDZ","isHasSpecifiedCard","zxIsCivilGudgement","isHasSpecialLoan","zxIsAcctBadDebt","zxIsHasQuasiCreditGDZ","zxIsHasCreditGDZ","zxIsCreCardStopPay","zxIsCarryRecord","zxWarrantLoanTypeUnnormal","zxIsSemiCreditRepayment","zxIsAccountRepayment","zxIsHasLoanInfo","zxPenaltyRecord","zxIsHasNormalCreditCard","zxIsHasCreditInfo","zxsLowInsurePersonType","zxLoanDelqStatus30Dayyues","zxSexFromZxPrcid"]';
expect_different = '["zxGuaranteeBal","zxGuaranteeCnt","zxRestDisposalBalaceAmt","zxRestDisposalCnt","zxsLoanUse","zxsUnclsCrdLegalbodyCnt","zxsDeclareCnt","zxIssuBankCorporateCnt","zxWarrantLoanRate1","zxWarrantLoanAmt","zxEndowBasicMoney","zxEndowRecentGetTime","zxWarrantLoanRate2","zxsCreCardGuaranteeIssuDate","zxsEndowBasicPayDate","zxsTelePayBusinessStartDate","zxsVehicleRecordMortgageFlag","zxWarrantLoanType"]';

same_json = json.loads(expect_same)
different_json = json.loads(expect_different)

expect_same_dict = {}
expect_different_dict = {}
expect_other_dict = {}

for key in same_json:
    conut_dict = {"取值相同" : 0, "取值不同" : 0, "身份证号" : []}
    expect_same_dict.setdefault(key, conut_dict)

for key in different_json:
    conut_dict = {"取值相同" : 0, "取值不同" : 0, "身份证号" : []}
    expect_different_dict.setdefault(key, conut_dict)

report_data = {'same' : expect_same_dict, 'different' : expect_different_dict, 'other' : expect_other_dict}

with open("/Users/x/Downloads/data") as data:
    for line in data:
        # print line
        line.strip()
        vars_json = json.loads(line)
        prcid = vars_json.keys()[0]
        value_dict = vars_json[prcid]
        same_var_list = value_dict['sameValueSet']
        different_var_list = value_dict['differentValueSet']
        first_gene_miss_var_list = value_dict['firstGeneMissValueSet']
        second_gene_miss_var_list = value_dict['secondGeneMissValueSet']
        both_miss_var_list = value_dict['bothMissValueSet']

        for var in same_var_list:
            if var in expect_same_dict:
                expect_same_dict[var]["取值相同"] = expect_same_dict[var]["取值相同"] + 1
                # if len(expect_same_dict[var]["身份证号"]) < 30:
                    # expect_same_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_different_dict:
                expect_different_dict[var]["取值相同"] = expect_different_dict[var]["取值相同"] + 1
                # if len(expect_different_dict[var]["身份证号"]) < 30:
                    # expect_different_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_other_dict:
                expect_other_dict[var]["取值相同"] = expect_other_dict[var]["取值相同"] + 1
                # if len(expect_other_dict[var]["身份证号"]) < 30:
                    # expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))
            else:
                # 不存在
                conut_dict = {"取值相同": 0, "取值不同": 0, "身份证号": []}
                expect_other_dict.setdefault(var, conut_dict)
                expect_other_dict[var]["取值相同"] = expect_other_dict[var]["取值相同"] + 1
                # if len(expect_other_dict[var]["身份证号"]) < 30:
                    # expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))

        for var in different_var_list:
            if var in expect_same_dict:
                expect_same_dict[var]["取值不同"] = expect_same_dict[var]["取值不同"] + 1
                if len(expect_same_dict[var]["身份证号"]) < 30:
                    expect_same_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_different_dict:
                expect_different_dict[var]["取值不同"] = expect_different_dict[var]["取值不同"] + 1
                if len(expect_different_dict[var]["身份证号"]) < 30:
                    expect_different_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_other_dict:
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))
            else:
                # 不存在
                conut_dict = {"取值相同": 0, "取值不同": 0, "身份证号": []}
                expect_other_dict.setdefault(var, conut_dict)
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))

        for var in first_gene_miss_var_list:
            if var in expect_same_dict:
                expect_same_dict[var]["取值不同"] = expect_same_dict[var]["取值不同"] + 1
                if len(expect_same_dict[var]["身份证号"]) < 30:
                    expect_same_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_different_dict:
                expect_different_dict[var]["取值不同"] = expect_different_dict[var]["取值不同"] + 1
                if len(expect_different_dict[var]["身份证号"]) < 30:
                    expect_different_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_other_dict:
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))
            else:
                # 不存在
                conut_dict = {"取值相同": 0, "取值不同": 0, "身份证号": []}
                expect_other_dict.setdefault(var, conut_dict)
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))

        for var in second_gene_miss_var_list:
            if var in expect_same_dict:
                expect_same_dict[var]["取值不同"] = expect_same_dict[var]["取值不同"] + 1
                if len(expect_same_dict[var]["身份证号"]) < 30:
                    expect_same_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_different_dict:
                expect_different_dict[var]["取值不同"] = expect_different_dict[var]["取值不同"] + 1
                if len(expect_different_dict[var]["身份证号"]) < 30:
                    expect_different_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_other_dict:
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))
            else:
                # 不存在
                conut_dict = {"取值相同": 0, "取值不同": 0, "身份证号": []}
                expect_other_dict.setdefault(var, conut_dict)
                expect_other_dict[var]["取值不同"] = expect_other_dict[var]["取值不同"] + 1
                if len(expect_other_dict[var]["身份证号"]) < 30:
                    expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))

        for var in both_miss_var_list:
            if var in expect_same_dict:
                expect_same_dict[var]["取值相同"] = expect_same_dict[var]["取值相同"] + 1
                # if len(expect_same_dict[var]["身份证号"]) < 30:
                    # expect_same_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_different_dict:
                expect_different_dict[var]["取值相同"] = expect_different_dict[var]["取值相同"] + 1
                # if len(expect_different_dict[var]["身份证号"]) < 30:
                    # expect_different_dict[var]["身份证号"].append(prcid.encode('ascii'))
            if var in expect_other_dict:
                expect_other_dict[var]["取值相同"] = expect_other_dict[var]["取值相同"] + 1
                # if expect_other_dict[var]["身份证号"] < 30:
                    # expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))
            else:
                # 不存在
                conut_dict = {"取值相同": 0, "取值不同": 0, "身份证号": []}
                expect_other_dict.setdefault(var, conut_dict)
                expect_other_dict[var]["取值相同"] = expect_other_dict[var]["取值相同"] + 1
                # if len(expect_other_dict[var]["身份证号"]) < 30:
                    # expect_other_dict[var]["身份证号"].append(prcid.encode('ascii'))

# 统计
for statistic_key in report_data:
    statistic_content = report_data[statistic_key]
    for statistic_var in statistic_content:
        total_count = statistic_content[statistic_var]["取值相同"] + statistic_content[statistic_var]["取值不同"]
        statistic_content[statistic_var]["总请求数"] = total_count
        if total_count != 0:
            statistic_content[statistic_var]["取值相同比例"] = round((statistic_content[statistic_var]["取值相同"] / total_count), 4)
            statistic_content[statistic_var]["取值不同比例"] = round((statistic_content[statistic_var]["取值不同"] / total_count), 4)
        else:
            statistic_content[statistic_var]["取值相同比例"] = 0
            statistic_content[statistic_var]["取值不同比例"] = 0

# dict输出到文件
pandas.DataFrame(report_data['same']).T.to_csv('/Users/x/Downloads/预期内取值一致变量.csv')
pandas.DataFrame(report_data['different']).T.to_csv('/Users/x/Downloads/预期内取值不一致变量.csv')
pandas.DataFrame(report_data['other']).T.to_csv('/Users/x/Downloads/梳理结果未覆盖变量.csv')
