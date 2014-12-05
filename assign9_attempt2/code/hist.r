data <- read.table("numpages", header=FALSE, sep='\n')
pdf("hist.pdf")
barplot(table(data), xlab = "Number of Pages", ylab = "Number of Blogs", main="Histogram- Number of Pages vs Blogs")
dev.off()
