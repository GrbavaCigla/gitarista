<!-- <div>
    <div class="input-group">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
            <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clip-rule="evenodd" />
        </svg>
        <input type="text" name="search" id="search" class="p-1.5">
        <button>Search</button>
    </div>
</div> -->
<div class="relative">
    <dir class="absolute p-2.5 inset-y-0 left-0 my-0">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="#4c566a"
            class="w-5 h-5"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
            />
        </svg>
    </dir>
    <label for="search" class="sr-only">Search</label>
    <input
        class="font-bold w-full rounded-xl focusable py-2 pl-10 pr-24 text-dark0"
        placeholder="Type your query here..."
        name="search"
        id="search"
    />
    <dir class="absolute right-0 inset-y-0 my-0">
        <button class="px-4 h-full text-primary-content rounded-r-xl font-bold bg-primary">Search</button>
    </dir>
</div>