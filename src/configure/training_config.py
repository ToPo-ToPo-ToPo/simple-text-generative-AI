
#======================================================================
# 使用できるdatasetの情報を設定する
# 辞書型 {group1: [name1, name2, ...], group2: [name1, name2, ...]}
#======================================================================
DATASETS_DICT = {
    "additional-sft": [
        "tyqiangz/multilingual-sentiments", 
    ],
    "instruction-sft": [
        "kunishou/databricks-dolly-15k-ja",
        "ToPo-ToPo/databricks-dolly-15k-ja-zundamon",
        "ToPo-ToPo/databricks-dolly-15k-ja-nanoja",
        "ToPo-ToPo/oasst1-89k-ja"
    ],
}