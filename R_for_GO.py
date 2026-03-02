#STEP 1: ติดตั้ง package
if (!require("BiocManager"))
    install.packages("BiocManager")

BiocManager::install("clusterProfiler")
BiocManager::install("org.Hs.eg.db")   # for human

#STEP 2: โหลด package
library(clusterProfiler)
library(org.Hs.eg.db)

#STEP 3: เตรียม gene list
gene_list <- c("TP53", "EGFR", "BRCA1", "MYC") #ข้างในวงเล็บใส่ชื่อ gene_nameของแต่ละ clusterที่เราสนใจได้เลย

#STEP 4: แปลง Gene Symbol → ENTREZ ID
gene_df <- bitr(gene_list,
                fromType = "SYMBOL",
                toType = "ENTREZID",
                OrgDb = org.Hs.eg.db)

gene_ids <- gene_df$ENTREZID

#STEP 5: ทำ GO enrichment
ego <- enrichGO(gene          = gene_ids,
                OrgDb         = org.Hs.eg.db,
                ont           = "BP",      # BP, MF, CC
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.05,
                qvalueCutoff  = 0.05,
                readable      = TRUE)

#STEP 6: ดูผลลัพธ์
head(ego)
หรือดูเป็นตาราง
as.data.frame(ego)

#STEP 7: Plot ผลลัพธ์
dotplot(ego)
barplot(ego, showCategory=10)

#STEP 8: Export to CSV
go_result <- as.data.frame(ego)
write.csv(go_result, "22_GO_result.csv", row.names = FALSE)
