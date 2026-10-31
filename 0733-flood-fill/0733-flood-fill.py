class Solution:
    def dfs(self,image,r,c,target_image,color):

        m=len(image)
        n=len(image[0])
        if r > m-1 or r< 0 or c > n-1 or c<0:
            return
        if target_image != image[r][c]:
            return 
        
        if image[r][c]==color:
            return
        if target_image == image[r][c]:
            image[r][c]=color
        


        self.dfs(image,r+1,c,target_image,color)
        self.dfs(image,r-1,c,target_image,color)
        self.dfs(image,r,c+1,target_image,color)
        self.dfs(image,r,c-1,target_image,color)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        target_color = image[sr][sc]
        m=len(image)
        n=len(image[0])
        self.dfs(image,sr,sc,target_color,color)
        return image

        