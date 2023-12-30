from discord.ext import commands
import discord
from dispie import Paginator                   # Used for changing content pages 


col = discord.Color.purple()


class DSA_visualizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_page = 0  # Initialize the current page to 0


# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

    @commands.group()
    async def visual_search(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to visual_search\n\nFor more info on a specific command, use {'*help*'} command```")    

    @commands.group()
    async def visual_sort(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to visual_search\n\nFor more info on a specific command, use {'*help*'} command```")    

    @commands.group()
    async def LL_visual(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to visual_search\n\nFor more info on a specific command, use {'*help*'} command```")    
    
    @commands.group()
    async def visual_stack(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to visual_search\n\nFor more info on a specific command, use {'*help*'} command```")    
    
    @commands.group()
    async def visual_queue(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to visual_search\n\nFor more info on a specific command, use {'*help*'} command```")    
    
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_search.command()
    async def linear_search(self, ctx: commands.Context):
        data = [
            {
                "description": """Now, let's see the working of the linear search Algorithm.

    To understand the working of the linear search algorithm, let's take an unsorted array. It will be easy to understand the working of linear search with an example.

    Let the element to be searched is K = 41""",
                "image_file": "https://i.imgur.com/fVJx0o8.png"  
            },
            
            {
                "description": """Now, start from the first element and compare K with each element of the array.

    The value of K, i.e., 41, is not matched with the first element of the array. So, move to the next element.""",
                "image_file": "https://i.imgur.com/KMayEaS.png"
            },
            
            {
                "description": """The value of K, i.e., 41, is not matched with the first element of the array. So, move to the next element.""",
                "image_file": "https://i.imgur.com/MeUjT33.png"
            },
            
            {
                "description": """The value of K, i.e., 41, is not matched with the first element of the array. So, move to the next element.""",
                "image_file": "https://i.imgur.com/FOoejlv.png"
            },
            
            {
                "description": """The value of K, i.e., 41, is not matched with the first element of the array. So, move to the next element.""",
                "image_file": "https://i.imgur.com/0rKY0vz.png"
            },
            
            {
                "description": """The value of K, i.e., 41, is not matched with the first element of the array. So, move to the next element.""",
                "image_file": "https://i.imgur.com/fBvmon9.png"
            },
            
            {
                "description": """Now, the element to be searched is found. So algorithm will return the index of the element matched.""",
                "image_file": "https://i.imgur.com/6QrfPRm.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
    
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_search.command()
    async def binary_search(self, ctx: commands.Context):
        data = [
            {
                "description": """In this algorithm, 

• Divide the search space into two halves by finding the middle index “mid”.

• Compare the middle element of the search space with the key. 

• If the key is found at middle element, the process is terminated.

• If the key is not found at middle element, choose which half will be used as the next search space.

    • If the key is smaller than the middle element, then the left side is used for next search.

    • If the key is larger than the middle element, then the right side is used for next search.

• This process is continued until the key is found or the total search space is exhausted.
""",
                "image_file": "https://i.imgur.com/AFy4awP.png"  
            },
            
            {
                "description": """Consider an array arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}, and the target = 23.
                
                First Step: Calculate the mid and compare the mid element with the key. If the key is less than mid element, move to left and if it is greater than the mid then move search space to the right.
                
                • Key (i.e., 23) is greater than current mid element (i.e., 16). The search space moves to the right.
""",
                "image_file": "https://i.imgur.com/e4f9So9.png"
            },
            
            {
                "description": """• Key is less than the current mid 56. The search space moves to the left.""",
                "image_file": "https://i.imgur.com/TWuc5gG.png"
            },
            
            {
                "description": """Second Step: If the key matches the value of the mid element, the element is found and stop search.""",
                "image_file": "https://i.imgur.com/7LNPgNc.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_sort.command()
    async def bubble_sort(self, ctx: commands.Context):
        data = [
            {
                "description": """In this algorithm, 

• traverse from left and compare adjacent elements and the higher one is placed at right side. 

• In this way, the largest element is moved to the rightmost end at first. 

• This process is then continued to find the second largest and place it and so on until the data is sorted.""",
                "image_file": ""  
            },
            
            {
                "description": """Input: arr[] = {6, 3, 0, 5}

First Pass: 

The largest element is placed in its correct position, i.e., the end of the array.""",
                "image_file": "https://i.imgur.com/a2dzRlE.png"
            },
            
            {
                "description": """Second Pass: 

Place the second largest element at correct position""",
                "image_file": "https://i.imgur.com/2OItehR.png"
            },
            
            {
                "description": """Third Pass:

Place the remaining two elements at their correct positions.""",
                "image_file": "https://i.imgur.com/CyXBXoK.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_sort.command()
    async def selection_sort(self, ctx: commands.Context):
        data = [
            {
                "description": """Lets consider the following array as an example: arr[] = {64, 25, 12, 22, 11}

First pass:

• For the first position in the sorted array, the whole array is traversed from index 0 to 4 sequentially. The first position where 64 is stored presently, after traversing whole array it is clear that 11 is the lowest value.

• Thus, replace 64 with 11. After one iteration 11, which happens to be the least value in the array, tends to appear in the first position of the sorted list.
""",
                "image_file": "https://i.imgur.com/aDSRiSm.png"  
            },
            
            {
                "description": """Second Pass:

• For the second position, where 25 is present, again traverse the rest of the array in a sequential manner.

• After traversing, we found that 12 is the second lowest value in the array and it should appear at the second place in the array, thus swap these values.
""",
                "image_file": "https://i.imgur.com/KpP9Dwv.png"
            },
            
            {
                "description": """Third Pass:

• Now, for third place, where 25 is present again traverse the rest of the array and find the third least value present in the array.

• While traversing, 22 came out to be the third least value and it should appear at the third place in the array, thus swap 22 with element present at third position.""",
                "image_file": "https://i.imgur.com/y3PnZjd.png"
            },
            
            {
                "description": """Fourth pass:

• Similarly, for fourth position traverse the rest of the array and find the fourth least element in the array 
• As 25 is the 4th lowest value hence, it will place at the fourth position.""",
                "image_file": "https://i.imgur.com/LvXxOZY.png"
            },
            
            {
                "description": """Fifth Pass:

• At last the largest value present in the array automatically get placed at the last position in the array
• The resulted array is the sorted array.""",
                "image_file": "https://i.imgur.com/emIGR24.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_sort.command()
    async def insertion_sort(self, ctx: commands.Context):
        data = [
            {
                "description": """The simple steps of achieving the insertion sort are listed as follows -

Step 1 - If the element is the first element, assume that it is already sorted. Return 1.

Step2 - Pick the next element, and store it separately in a key.

Step3 - Now, compare the key with all elements in the sorted array.

Step 4 - If the element in the sorted array is smaller than the current element, then move to the next element. Else, shift greater elements in the array towards the right.

Step 5 - Insert the value.

Step 6 - Repeat until the array is sorted.""",
                "image_file": ""  
            },
            
            {
                "description": """Now, let's see the working of the insertion sort Algorithm.

To understand the working of the insertion sort algorithm, let's take an unsorted array. It will be easier to understand the insertion sort via an example.

Let the elements of array""",
                "image_file": "https://i.imgur.com/F2CfCfT.png"
            },
            
            {
                "description": """Initially, the first two elements are compared in insertion sort.
""",
                "image_file": "https://i.imgur.com/HOIWyyz.png"
            },
            
            {
                "description": """Here, 31 is greater than 12. That means both elements are already in ascending order. So, for now, 12 is stored in a sorted sub-array.
""",
                "image_file": "https://i.imgur.com/AGJtQaX.png"
            },
            
            {
                "description": """Now, move to the next two elements and compare them.""",
                "image_file": "https://i.imgur.com/cIXzEY0.png"
            },
            
            {
                "description": """Here, 25 is smaller than 31. So, 31 is not at correct position. Now, swap 31 with 25. Along with swapping, insertion sort will also check it with all elements in the sorted array.

For now, the sorted array has only one element, i.e. 12. So, 25 is greater than 12. Hence, the sorted array remains sorted after swapping.""",
                "image_file": "https://i.imgur.com/z1QaoPm.png"
            },
            
            {
                "description": """Now, two elements in the sorted array are 12 and 25. Move forward to the next elements that are 31 and 8.""",
                "image_file": "https://i.imgur.com/e6818U2.png"
            },
            
            {
                "description": """Both 31 and 8 are not sorted. So, swap them.
""",
                "image_file": "https://i.imgur.com/SKeUyQm.png"
            },
            
            {
                "description": """After swapping, elements 25 and 8 are unsorted.
                
So, swap them.""",
                "image_file": "https://i.imgur.com/oUTYaPX.png"
            },
            
            {
                "description": """Now, elements 12 and 8 are unsorted.

So, swap them too.""",
                "image_file": "https://i.imgur.com/GIHBIju.png"
            },
            
            {
                "description": """Now, the sorted array has three items that are 8, 12 and 25. Move to the next items that are 31 and 32.""",
                "image_file": "https://i.imgur.com/wi9BO2y.png"
            },
            
            {
                "description": """Hence, they are already sorted. Now, the sorted array includes 8, 12, 25 and 31.
""",
                "image_file": "https://i.imgur.com/BFw1Iao.png"
            },
            
            {
                "description": """Move to the next elements that are 32 and 17.
                
17 is smaller than 32. So, swap them""",
                "image_file": "https://i.imgur.com/r1e4QAw.png"
            },
            
            {
                "description": """Swapping makes 31 and 17 unsorted. So, swap them too.
""",
                "image_file": "https://i.imgur.com/g82NKvG.png"
            },
            
            {
                "description": """Now, swapping makes 25 and 17 unsorted. So, perform swapping again.
                
Now, the array is completely sorted.
""",
                "image_file": "https://i.imgur.com/gzLjKB2.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_sort.command()
    async def quick_sort(self, ctx: commands.Context):
        data = [
            {
                "description": """To understand the working of quick sort, let's take an unsorted array. It will make the concept more clear and understandable.

Let the elements of array are""",
                "image_file": "https://i.imgur.com/rWK0ziV.png"  
            },
            
            {
                "description": """In the given array, we consider the leftmost element as pivot. So, in this case, a[left] = 24, a[right] = 27 and a[pivot] = 24.

Since, pivot is at left, so algorithm starts from right and move towards left.""",
                "image_file": "https://i.imgur.com/DS5f0vS.png"
            },
            
            {
                "description": """Now, a[pivot] < a[right], so algorithm moves forward one position towards left, i.e. -""",
                "image_file": "https://i.imgur.com/zBGiPbr.png"
            },
            
            {
                "description": """Now, a[left] = 24, a[right] = 19, and a[pivot] = 24.

Because, a[pivot] > a[right], so, algorithm will swap a[pivot] with a[right], and pivot moves to right, as -""",
                "image_file": "https://i.imgur.com/f7fV2IF.png"
            },
            
            {
                "description": """Now, a[left] = 19, a[right] = 24, and a[pivot] = 24. Since, pivot is at right, so algorithm starts from left and moves to right.

As a[pivot] > a[left], so algorithm moves one position to right as -""",
                "image_file": "https://i.imgur.com/46wc6QS.png"
            },
            
            {
                "description": """Now, a[left] = 9, a[right] = 24, and a[pivot] = 24. As a[pivot] > a[left], so algorithm moves one position to right as -""",
                "image_file": "https://i.imgur.com/lqjx8pG.png"
            },
            
            {
                "description": """Now, a[left] = 29, a[right] = 24, and a[pivot] = 24. As a[pivot] < a[left], so, swap a[pivot] and a[left], now pivot is at left, i.e. -""",
                "image_file": "https://i.imgur.com/9JdYmgx.png"
            },
            
            {
                "description": """Since, pivot is at left, so algorithm starts from right, and move to left. Now, a[left] = 24, a[right] = 29, and a[pivot] = 24. As a[pivot] < a[right], so algorithm moves one position to left, as -""",
                "image_file": "https://i.imgur.com/uk8HIOp.png"
            },
            
            {
                "description": """Now, a[pivot] = 24, a[left] = 24, and a[right] = 14. As a[pivot] > a[right], so, swap a[pivot] and a[right], now pivot is at right, i.e. -""",
                "image_file": "https://i.imgur.com/oKeZgm7.png"
            },
            
            {
                "description": """Now, a[pivot] = 24, a[left] = 14, and a[right] = 24. Pivot is at right, so the algorithm starts from left and move to righ""",
                "image_file": "https://i.imgur.com/ZZLvw4c.png"
            },
            
            {
                "description": """Now, a[pivot] = 24, a[left] = 24, and a[right] = 24. So, pivot, left and right are pointing the same element. It represents the termination of procedure.

Element 24, which is the pivot element is placed at its exact position.

Elements that are right side of element 24 are greater than it, and the elements that are left side of element 24 are smaller than it.""",
                "image_file": "https://i.imgur.com/vo643y6.png"
            },
            
            {
                "description": """Now, in a similar manner, quick sort algorithm is separately applied to the left and right sub-arrays. After sorting gets done, the array will be -""",
                "image_file": "https://i.imgur.com/1TYnhgh.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_sort.command()
    async def merge_sort(self, ctx: commands.Context):
        data = [
            {
                "description": """Now, let's see the working of merge sort Algorithm.

To understand the working of the merge sort algorithm, let's take an unsorted array. It will be easier to understand the merge sort via an example.

Let the elements of array are -

""",
                "image_file": "https://i.imgur.com/OWuL6Dc.png"  
            },
            
            {
                "description": """According to the merge sort, first divide the given array into two equal halves. Merge sort keeps dividing the list into equal parts until it cannot be further divided.

As there are eight elements in the given array, so it is divided into two arrays of size 4.""",
                "image_file": "https://i.imgur.com/sfx6QzW.png"
            },
            
            {
                "description": """Now, again divide these two arrays into halves. As they are of size 4, so divide them into new arrays of size 2.""",
                "image_file": "https://i.imgur.com/C7FWHR3.png"
            },
            
            {
                "description": """Now, again divide these arrays to get the atomic value that cannot be further divided.""",
                "image_file": "https://i.imgur.com/Uw4bjzS.png"
            },
            
            {
                "description": """Now, combine them in the same manner they were broken.

In combining, first compare the element of each array and then combine them into another array in sorted order.

So, first compare 12 and 31, both are in sorted positions. Then compare 25 and 8, and in the list of two values, put 8 first followed by 25. Then compare 32 and 17, sort them and put 17 first followed by 32. After that, compare 40 and 42, and place them sequentially.""",
                "image_file": "https://i.imgur.com/tLfEySH.png"
            },
            
            {
                "description": """In the next iteration of combining, now compare the arrays with two data values and merge them into an array of found values in sorted order.""",
                "image_file": "https://i.imgur.com/mmkW4iD.png"
            },
            
            {
                "description": """Now, there is a final merging of the arrays. After the final merging of above arrays, the array will look like -""",
                "image_file": "https://i.imgur.com/NvCnech.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col)

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def singly_insertion(self, ctx: commands.Context):
        data = [
            {
                "title": "Insertion At Beginning",
                "description": """Imagine our linked list is not necessarily sorted and there is no reason to insert a new node in any special place in the list. Then we have an easiest place to insert the node is at the beginning of the list.  An algorithm that does so follows.

Algorithm of insertion at the beginning:    

    • Create a new node
    • Assign its data value
    • Assign newly created node’s next ptr to current head reference. So, it points to the previous start node of the linked list address
    • Change the head reference to the new node’s address.""",
                "image_file": "https://i.imgur.com/ilSsXir.png"  
            },
            
            {
                "title": "Insertion At Ending",
                "description": """To insert element in linked list last we would use the following steps to insert a new Node at the last of the doubly linked list:

    • Create a new node
    • Assign its data value
    • Assign its next node to NULL as this will be the last(tail) node
    • Check if the list is empty
        • Change the head node to the new node
    • If not then traverse till the last node
    • Assign the last node’s next pointer to this new node
    • Now, the new node has become the last node.""",
                "image_file": "https://i.imgur.com/bMUFXsF.png"
            },
            
            {
                "title": "Insertion At Specified Position",
                "description": """First we will create a new node named by newnode and put the position where u want to insert the node.

Now give the address of the new node in previous node means link the new node with previous node.

After this, give the address of current node in new node.Means link your new node also with current node.""",
                "image_file": "https://i.imgur.com/npjDH8p.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def singly_deletion(self, ctx: commands.Context):
        data = [
            {
                "title": "Deletion At Beginning",
                "description": """• Move the current head from 1st node to the next node
                
• Delete the first node using the free method

• If the Linked List is empty that it is not possible to delete""",
                "image_file": "https://i.imgur.com/YqBtQ02.png"  
            },
            
            {
                "title": "Deletion At Ending",
                "description": """
• If the Linked list has only one node then make head node null
• Else traverse to the end of the linked list
• While traversing store the previous node i.e. 2nd last node
• Change the next of 2nd last node to null
• Free/delete memory of the the last node
• Now, 2nd last node becomes the last node.""",
                "image_file": "https://i.imgur.com/F2RpL7O.png"
            },
            
            {
                "title": "Deletion At Specified Position",
                "description": """• Accept the position from the user to delete
• If it is the first node to delete, change the head to the next node and free the first node memory.
• While traversing to the nth node, always store the previous (n-1)th node
• Assign next of (n-1)th node to nth node’s next i.e. (n+1)th node
• Free the memory for nth node.""",
                "image_file": "https://i.imgur.com/dB0RWPe.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def doubly_insertion(self, ctx: commands.Context):
        data = [
            {
                "title": "Insertion At Beginning",
                "description": """In the doubly linked list, we would use the following steps to insert a new node at the beginning of the doubly linked list:


• Create a new node

• Assign its data value

• Assign newly created node’s next ptr to current head reference. So, it points to the previous start node of the linked list address

• Change the head reference to the new node’s address.

• Change the next node’s previous pointer to new node’s address (head reference)""",
                "image_file": "https://i.imgur.com/sE46qaH.png"  
            },
            
            {
                "title": "Insertion At Ending",
                "description": """In insertion, at the last node, we would use the following steps to insert a new Node at the last of the doubly linked list.


• Create a new node

• Assign its data value

• Assign its next node to NULL as this will be the last(tail) node

• Check if the list is empty

    • Change the head node to this node

    • If it is empty then just assign the previous node as NULL and return

• If not then traverse till the last node

• Assign the last node’s next pointer to this new node

• Assing this new node’s previous to the last node in the list

• Now, the new node has become the last node.""",
                "image_file": "https://i.imgur.com/ZhSQ1rU.png"
            },
            
            {
                "title": "Insertion At Specified Position",
                "description": """• Calculate the size of the node

• If the position you want to enter is less than 1

    • Invalid position But, if 0 then use insertAtStart method

• If the position you want to enter is greater than size then
    
    • Invalid position, but if the position is equal to size then use insertLast method 

• else create a temp node and assign it the address of the head

• Create a new node and assign it the data value

• Iterate to the position you want to enter after in the linked list

• Assign this new node’s next and previous nodes

• Assign previous node’s next to this new node

• Assign next node’s previous to this new node""",
                "image_file": "https://i.imgur.com/CysWPIQ.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def doubly_deletion(self, ctx: commands.Context):
        data = [
            {
                "title": "Deletion At Beginning",
                "description": """• Check if there is only 1 node or not
                
• If there is one node
    
    • Assign head to NULL

    • Free memory

• Else
    
    • Assign head to next node in the list
    
    • Assign head->prev to NULL

    • Free memory""",
                "image_file": "https://i.imgur.com/ACwvuGx.png"  
            },
            
            {
                "title": "Deletion At Ending",
                "description": """• Traverse till the target node

• Check if this is the last node i.e. if node->next = NULL, then its last node

• Assign last node’s previous node’s next pointer to the last node’s next node’s address, which basically is NULL in this case

• Free the memory""",
                "image_file": "https://i.imgur.com/4yzUrsk.png"
            },
            
            {
                "title": "Deletion At Specified Position",
                "description": """• Traverse till the target node

• create a node called the previous storing previous node of the target node

• Assign previous node’s next pointer to the next node of the target node

• For the next node of the target node, its previous pointer is assigned to the targets node’s previous node’s address

• Free memory of target node""",
                "image_file": "https://i.imgur.com/jTW5i6Z.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def circular_insertion(self, ctx: commands.Context):
        data = [
            {
                "title": "Insertion At Beginning",
                "description": """Make the linked list.
                
Then we have to take an extra pointer which points to the end node of the circular linked list.

Then we have a pointer that is pointing to the end node, then end node-> next will point to the first node.

At last follow the algorithm for insertion at beginning in circular linked list given below.""",
                "image_file": "https://i.imgur.com/NBrTg08.png"  
            },
            
            {
                "title": "Insertion At Ending",
                "description": """• Make a new node.

• Assign the new node next to circular list.

• If the list is empty then return new node.

• Assign the new node next to the front of the list.

• Assign tail next to the new node.

• Return the end node of the circular linked list.""",
                "image_file": "https://i.imgur.com/ynWcxAQ.png"
            },
            
            {
                "title": "Insertion At Specified Position",
                "description": """• Make a new node and set the data.

• Move to pos-1 position in the circular linked list.

• Now link the next pointer of new node with the node pointed by the next pointer of current(pos-1) node.

• After that join the next pointer of current node with the newly created node which means that the next pointer of current node will point to new node.

• Now print the linked list.

• Learn algorithm given below to understand better.""",
                "image_file": "https://imgur.com/6N98801"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @LL_visual.command()
    async def circular_deletion(self, ctx: commands.Context):
        data = [
            {
                "title": "Deletion At Beginning",
                "description": """Algorithm for deletion from beginning of a circular linked list:
                
deleteFirst()

IF head == null

    return

ELSE IF head != tail

    head = head -> next
    
    tail -> next = head

ELSE
    
    head = tail = null""",
                "image_file": "https://i.imgur.com/PlCltdV.png"  
            },
            
            {
                "title": "Deletion At Ending",
                "description": """Algorithm for deletion from last of a circular linked list:
                
deleteLast()

IF head == null
    
    return

ELSE IF head != tail

    Node current = head

    WHILE current->next != tail
        
        current = current-> next
        
        tail = current;
        
        tail-> next = head
ELSE

    head = tail = null""",
                "image_file": "https://i.imgur.com/qd3gkyq.png"
            },
            
            {
                "title": "Deletion At Specified Position",
                "description": """Algorithm for deletion from last of a circular linked list:
                
deleteLast()

IF head == null

    return

ELSE
    
    WHILE (–n>0)
        
        previous = temp;
        
        temp = temp.next;
    
    previous.next = temp.next;""",
                "image_file": "https://i.imgur.com/prwx9jr.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_stack.command()
    async def stack_visual(self, ctx: commands.Context):
        data = [
            {
                "title": "Stack and its operations",
                "description": """• Stack can be defined as a Data Structure that serves as saving the data in a particular fashion.

• In linear data structures like an array and linked list a user is allowed to insert or delete any element to and from any location respectively.

• However, in a Stack, both, insertion and deletion, is permitted at one end only.

• A Stack works on the LIFO (Last In – First Out) basis, i.e, the first element that is inserted in the stack would be the last to be deleted; or the last element to be inserted in the stack would be the first to be deleted.


Stack Operations

1. Push: Adding a new item to the Stack Data Structure, in other words pushing new item to Stack DS.
If Stack is full, then it is said to be in an overflow condition

2. Pop: Removing an item from the stack, i.e. popping an item out.
If a stack is empty then it is said to be in an underflow condition

3.Peek: This basically returns the topmost item in the stack, in other words, peek that what is the topmost item.

4.IsEmpty: This returns True If the stack is empty else returns False""",
                "image_file": ""  
            },
            
            {
                "title": "Push Operation",
                "description": """• Check whether stack is full or not.
                
• If the stack is full, it is not possible to add another element.

• Otherwise, create new node, store the data and change the pointer of top to the newly created node.""",
                "image_file": "https://i.imgur.com/vdlKr2X.png"
            },
            
            {
                "title": "Pop Operation",
                "description": """• In case of pop, note whether the stack is empty or not.

• It is not possible to remove element if the stack is empty.

• Else, store the top variable in temp and make top point to the next variable and delete temp.""",
                "image_file": "https://i.imgur.com/yytWbDz.png"
            },
            
            {
                "title": "Top/Peek Operation",
                "description": """• This operation returns the top most or peak element of the stack.

• The value of top changes with each push() or pop() operation.""",
                "image_file": "https://i.imgur.com/Dqb9Ots.png"
            },
            
            {
                "title": "IsEmpty Operation",
                "description": """• This operation returns true if the stack is found to be empty.

• Empty stack symbolizes that top = -1.""",
                "image_file": "https://i.imgur.com/by4Noqy.png"
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @visual_queue.command()
    async def queue_visual(self, ctx: commands.Context):
        data = [
            {
                "title": "Queue and its operations",
                "description": """• Unlike arrays, where insertion and deletion can happen at any end.

• In Queues, insertion (Enqueue) and deletion (Dequeue) can happen at only one end each.

• Insertion happens at the rear end and deletion happens at the front

• Queues follow FIFO First in First out structure, i.e. the element added first (Enqueued) will go out of the queue first(Dequeued)

• Unlike stack, which follows, LIFO, last in first out, and stack where both insertion and deletion happens as one end. For queue insertion(Enqueue) and deletion(Dequeue) happens at opposite ends. 



*Queue Operations*

1. Enqueue: Adding a new item to the Queue Data Structure, in other words, enqueuing new item to Stack DS.
If the Queue is full, then it is said to be in an overflow condition

2. Dequeue: Removing an item from the Queue, i.e. dequeuing an item out.
If a Queue is empty then it is said to be in an underflow condition

3. IsEmpty: This returns True If the Queue is empty else returns False

4. IsFull: This returns True if the Queue is full else returns false.""",
                "image_file": "https://i.imgur.com/eHZk4Jq.png"  
            },
            
            {
                "title": "Enqueue Operation",
                "description": """• When we require to add an element to the Queue we perform Enqueue() operation.

• Push() operation is synonymous of insertion/addition in a data structure.""",
                "image_file": "https://i.imgur.com/VYtAPPl.png"
            },
            
            {
                "title": "Dequeue Operation",
                "description": """• When we require to delete/remove an element to the Queue we perform Dequeue() operation.

• Dequeue() operation is synonymous of deletion/removal in a data structure.""",
                "image_file": "https://i.imgur.com/7heSKGI.png"
            },
            
            {
                "title": "Top/Peek Operation",
                "description": """The peek() method returns the object at the top of the current queue, without removing it. If the queue is empty this method returns null.""",
                "image_file": "https://i.imgur.com/1JU5SxB.png"
            },
            
            {
                "title": "IsEmpty Operation",
                "description": """This operation returns a boolean value that indicates whether the queue is empty or not.

The following steps are taken to perform the Empty operation:

    • check if front value is equal to -1 or not, if yes then return true means queue is empty.
    • Otherwise return false, means queue is not empty""",
                "image_file": ""
            }
        ]

        embeds = []

        for page_data in data:
            embed = discord.Embed(description=page_data["description"], colour=col, title=page_data["title"])

            # Attach the image file to the message
            embed.set_image(url=page_data['image_file'])
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)

            embeds.append(embed)

        pages = Paginator(embeds)  # Paginating through a list of items in embed

        # Send the paginated message
        message = await pages.start(ctx)
        
        
                
                
async def setup(bot):
    await bot.add_cog(DSA_visualizer(bot))
