const MenuBtn = ({menuBtnLightRef}) => {
    return (
        <>
            <svg width="40" height="40" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g id="menuBtn">
                <g id="menuBtnDark">
                <g id="base" filter="url(#filter0_i_9_20)">
                <circle cx="50" cy="50" r="50" fill="#1E1E1E"/>
                </g>
                <g id="lines" filter="url(#filter1_d_9_20)">
                <path id="Line 21" d="M25 50H75" stroke="white" stroke-width="5" stroke-linecap="round"/>
                <path id="Line 22" d="M25 70H75" stroke="white" stroke-width="5" stroke-linecap="round"/>
                <path id="Line 23" d="M25 30H75" stroke="white" stroke-width="5" stroke-linecap="round"/>
                </g>
                </g>
                <g id="menuBtnLight" ref={menuBtnLightRef}>
                <g id="base_2" filter="url(#filter2_i_9_20)">
                <circle cx="50" cy="50" r="50" fill="white"/>
                </g>
                <g id="lines_2" filter="url(#filter3_d_9_20)">
                <path id="Line 21_2" d="M25 50H75" stroke="black" stroke-width="5" stroke-linecap="round"/>
                <path id="Line 22_2" d="M25 70H75" stroke="black" stroke-width="5" stroke-linecap="round"/>
                <path id="Line 23_2" d="M25 30H75" stroke="black" stroke-width="5" stroke-linecap="round"/>
                </g>
                </g>
                </g>
                <defs>
                <filter id="filter0_i_9_20" x="0" y="0" width="100" height="104" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
                <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                <feOffset dy="4"/>
                <feGaussianBlur stdDeviation="2"/>
                <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
                <feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.25 0"/>
                <feBlend mode="normal" in2="shape" result="effect1_innerShadow_9_20"/>
                </filter>
                <filter id="filter1_d_9_20" x="18.5" y="27.5" width="63" height="53" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                <feOffset dy="4"/>
                <feGaussianBlur stdDeviation="2"/>
                <feComposite in2="hardAlpha" operator="out"/>
                <feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.25 0"/>
                <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_9_20"/>
                <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_9_20" result="shape"/>
                </filter>
                <filter id="filter2_i_9_20" x="0" y="0" width="100" height="104" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
                <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                <feOffset dy="4"/>
                <feGaussianBlur stdDeviation="2"/>
                <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
                <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
                <feBlend mode="normal" in2="shape" result="effect1_innerShadow_9_20"/>
                </filter>
                <filter id="filter3_d_9_20" x="18.5" y="27.5" width="63" height="53" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                <feOffset dy="4"/>
                <feGaussianBlur stdDeviation="2"/>
                <feComposite in2="hardAlpha" operator="out"/>
                <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
                <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_9_20"/>
                <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_9_20" result="shape"/>
                </filter>
                </defs>
            </svg>
        </>

    )
};

export default MenuBtn;