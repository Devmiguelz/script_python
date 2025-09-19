from bs4 import BeautifulSoup

def save_links_to_txt(links: list[str], filename: str, separator: str = "\n"):
    """
    Guarda los links en un archivo .txt
    :param links: lista de URLs
    :param filename: nombre del archivo .txt
    :param separator: "\n" para línea por línea, "|" para separados por |
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(separator.join(links))


html = """<div id="contents" class="style-scope ytd-rich-grid-renderer"><ytd-rich-item-renderer
        class="style-scope ytd-rich-grid-renderer" items-per-row="4" lockup="true" rendered-from-rich-grid=""
        is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/vUPAD4Bv7gU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/vUPAD4Bv7gU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBzjehxSX-ATdb-l4xZL3mJ3A21tA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/vUPAD4Bv7gU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Got Caught Stealing (dre_da_dancer)" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Got Caught Stealing (dre_da_dancer)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">12&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/J7J892accGg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/J7J892accGg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD7PSqAiqDmHT1Rg-Pnr1GAW9aOnQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/J7J892accGg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Judged Too Soon 😤💪 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Judged Too Soon 😤💪 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">10&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/tYpUaltS0_c"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/tYpUaltS0_c/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDaZshH84SI-4k7pHh59kbpKP6Cng">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/tYpUaltS0_c"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="When the Teacher Went Off (@campus.univers.cascades)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">When the Teacher Went Off (@campus.univers.cascades)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">12&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/_oHVSBxibJQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/_oHVSBxibJQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBZsMj4p8TUL2pfwwp9i2DhdJK6mg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/_oHVSBxibJQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Almost Won, Until This Happened! (@boys.club35)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Almost Won, Until This Happened! (@boys.club35)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/iFfkauNAb3Q"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/iFfkauNAb3Q/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD4HkUIxsRQXvg4BY-Qy9NQGjf09w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/iFfkauNAb3Q"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Wait for the Speed at the End! 😱🔥 #shorts"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Wait for the Speed at the End! 😱🔥 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">6,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/D7lVmk3J8QU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/D7lVmk3J8QU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC_lvpOo8nc-vf_eXx1S2XzZTkfUA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/D7lVmk3J8QU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="The Craziest Finish Ever (@officialtransagulhas) #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">The Craziest Finish Ever (@officialtransagulhas) #shorts</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">6,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/v6Wt1O9TURQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/v6Wt1O9TURQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAVBw1wYSM2LUv8vx8MpMrMYyjz1w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/v6Wt1O9TURQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Prank Went Horribly Wrong Until… (@dosrayos3) #shorts"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Prank Went Horribly Wrong Until… (@dosrayos3) #shorts</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/v6YD8ayMTWk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/v6YD8ayMTWk/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDB-1gNeghoR3VkrGByPpD2Yq3M6g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/v6YD8ayMTWk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/vJzmFqq7h5o"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/vJzmFqq7h5o/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBhR1Ej5GUweuXzu4ZSDi-GxokWYg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/vJzmFqq7h5o"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Ran When She Revealed Herself 😱 (@unkn8645)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Ran When She Revealed Herself 😱 (@unkn8645)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/VIoRQh5gZ1g"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/VIoRQh5gZ1g/oardefault.jpg?sqp=-oaymwEoCJQDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCC7DP0ZUvEN8M8vY1K8R_e823jGg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/VIoRQh5gZ1g"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Nurse Saved The Fighter Life! #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Nurse Saved The Fighter Life! #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/_E-bcjPg3kw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/_E-bcjPg3kw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCpDOWd2rQcwlbF3or5FKcwo1iJrg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/_E-bcjPg3kw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/q5BCWWjDgWo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/q5BCWWjDgWo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDsCb3Yp7PheTVITXrJYpeMTHmffQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/q5BCWWjDgWo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Uei7xSg5V_E"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Uei7xSg5V_E/oardefault.jpg?sqp=-oaymwEoCJYDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCsic0RG5FzzeWFheUvTYWXjpwWdA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Uei7xSg5V_E"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/RfvWOoYSn-E"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/RfvWOoYSn-E/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCO3T81g-fCWVrNQ8ZjEQytHmL_UA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/RfvWOoYSn-E"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/wwCBuDWOZVM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/wwCBuDWOZVM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCTxKSOhBuXbcRgWNnzWH0b1Lo_IQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/wwCBuDWOZVM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/7V42u8JczwY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/7V42u8JczwY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCfs5nZnn-JBPkzQpayQn4zRNtffQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/7V42u8JczwY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/TCwHOyeh9Wo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/TCwHOyeh9Wo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA5y1i02dGj_Kn3XpkoIJC7hJ3B_g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/TCwHOyeh9Wo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/f_u_lXwd4wI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/f_u_lXwd4wI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDrf0iyusY5TiIY7Ew97g3VmIRbUQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/f_u_lXwd4wI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Made Post Malone Famous #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Made Post Malone Famous #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/cEEiqTNOFBM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/cEEiqTNOFBM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAsr27l3iUaAUKYk7ckUFfuAXdd9A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/cEEiqTNOFBM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/LDX9kgxm0lg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/LDX9kgxm0lg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAmCRbZb5VAKv5OdUH4NuJ6CUIhWg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/LDX9kgxm0lg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/MIFYkVUBc6I"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/MIFYkVUBc6I/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBkGXwEqRVP_FnM5alDexef9KrGGQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/MIFYkVUBc6I"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="The Ultimate Comeback! 🔥 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">The Ultimate Comeback! 🔥 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/qRkM1PKp-EQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/qRkM1PKp-EQ/oardefault.jpg?sqp=-oaymwEoCJQDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBQPReo__52RGfWzzKVh-CmULOJYA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/qRkM1PKp-EQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ZNfOnso-Vj0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ZNfOnso-Vj0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB1Oz_CpSyNbuUDRJlrlQGiQamLmw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ZNfOnso-Vj0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/BJ58v0mEx7U"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/BJ58v0mEx7U/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBPOdi4zWQblackR-25TJTBcn52LQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/BJ58v0mEx7U"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Caught on Camera 😱 (@uekan2b) #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Caught on Camera 😱 (@uekan2b) #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/OSd2lLmGGgA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/OSd2lLmGGgA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAmPGne6vr4sK-dtPeHm7Dij7OXAw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/OSd2lLmGGgA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Did Something Unexpected 😲 (@yg_basketball)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Did Something Unexpected 😲 (@yg_basketball)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/tSFxgwF9Zrg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/tSFxgwF9Zrg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDnjUvhjQg9VEBbJC7uLG1eTAx8Rg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/tSFxgwF9Zrg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/asM3DuAtjwc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/asM3DuAtjwc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLABWmQkZ9RTodvd4iXSe5O0Rpv7dA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/asM3DuAtjwc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/d8RbxYCh3CY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/d8RbxYCh3CY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD0ftVjb0B5t-0nqIUyTT7dUTwaJw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/d8RbxYCh3CY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/QBJx8vPB_jY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/QBJx8vPB_jY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA4xGdeRwMxpwWUg6QBnWZMpedxGg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/QBJx8vPB_jY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Yrfv9ui2yCU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Yrfv9ui2yCU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBLhzLLcS0PozzmEQStAcTrYcRPXw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Yrfv9ui2yCU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Cyclist Saves Cat in Final Seconds (@smrty_ian) #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Cyclist Saves Cat in Final Seconds (@smrty_ian) #shorts</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/m4fsTDcqzFA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/m4fsTDcqzFA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAWoELzf6XRDPceG_Eq6SA8YBk1jA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/m4fsTDcqzFA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/_D3-nXR-FFU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/_D3-nXR-FFU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAdYd7eJtxp2xrvt0bg3P2MNn3AgA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/_D3-nXR-FFU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/pf0o_9VQfLo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/pf0o_9VQfLo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBCsZf2Z03k5PrMSOU-QsGSoJBFEQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/pf0o_9VQfLo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/S5ggMiR-wcE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/S5ggMiR-wcE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD41FOujDQZ-yIJilw-MirXjD14GQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/S5ggMiR-wcE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/5XgHqOv4WBs"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/5XgHqOv4WBs/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAsc5gvdQE4uesyO795LLJrsK31cA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/5XgHqOv4WBs"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="This Player is a Legend for This 😊 (@goleafsg0) #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">This Player is a Legend for This 😊 (@goleafsg0) #shorts</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/QlgDWwqvvEE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/QlgDWwqvvEE/oardefault.jpg?sqp=-oaymwEoCJQDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCGjzG0UV2XwKH3UpzCpf78mfZsew">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/QlgDWwqvvEE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Wh-Q_9PvOXg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Wh-Q_9PvOXg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCeLh-4zqtg6gwIHKHSJfVkJy3sFQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Wh-Q_9PvOXg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/WyItQ1FQ8lM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/WyItQ1FQ8lM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC5BaaAe6SEz5p-gqEocR4T-0Dwmg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/WyItQ1FQ8lM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ir_iUT_X5lc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ir_iUT_X5lc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCxPBnKhNkpE5nhtbVybux-eo0PIg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ir_iUT_X5lc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="She Didn't Stop for Her Family 😤 #shorts"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">She Didn't Stop for Her Family 😤 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/u8Pt78XBYsU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/u8Pt78XBYsU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDVPoU0ubtyMmonWcoOg-L1p3Tr7w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/u8Pt78XBYsU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/_Z-30QqNP0g"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/_Z-30QqNP0g/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCPt70v4uHO-C14wRqfnBn9ulKmzQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/_Z-30QqNP0g"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Su7LrV_cfwY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Su7LrV_cfwY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB3cxQa66GdWA2sw-6EosuOd_wbHg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Su7LrV_cfwY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/OY_CCajkwB8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/OY_CCajkwB8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDmo5yQtgfSb0wyaHfnfQI-antVHw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/OY_CCajkwB8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,8&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Vw3Fahzvjpo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Vw3Fahzvjpo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDjubVRrt3qexWvcZYkSHQG-b4aJA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Vw3Fahzvjpo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,8&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/QVlbhUK8vQ0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/QVlbhUK8vQ0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDhN5ENcRjFojvIPLiT4M-o-Z5EhA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/QVlbhUK8vQ0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/waLn9A_6huI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/waLn9A_6huI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBFjHs8_zzrvQ9fWzwYa9R3J1-DVA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/waLn9A_6huI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/4OUUVdXoI_8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/4OUUVdXoI_8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAwyn303d5UZOYN5tvFgx1I4s2T0A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/4OUUVdXoI_8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,9&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/hqz5xKWFltc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/hqz5xKWFltc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDHOERA-JkZicwPX1XuFW97ol02rA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/hqz5xKWFltc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Gak5SVkVEYc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Gak5SVkVEYc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAUB05J6uGC95f36ApaZS9uERgqrw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Gak5SVkVEYc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PCPXhwu2N1c"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PCPXhwu2N1c/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDyjKbk8RPX0prkjBlptrDiqZqZjQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PCPXhwu2N1c"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/y8AbJEDiZHE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/y8AbJEDiZHE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB6cg32vktXPlArRnC7odkvW0yqOw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/y8AbJEDiZHE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/NFBFSDrEr_U"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/NFBFSDrEr_U/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLASxQuB0l87AYD9JH7P_xhIDfTTgQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/NFBFSDrEr_U"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/8HMI5JI9J3Q"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/8HMI5JI9J3Q/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBEH-MogZ2BcDu0O7EFCya8o9_Z0w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/8HMI5JI9J3Q"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="They Set a World Record 😱 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">They Set a World Record 😱 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,7&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/w96Y6SG84Vk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/w96Y6SG84Vk/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBX0OfcNZ2xhAVRvVfs-Gu1kgl_Cw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/w96Y6SG84Vk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/5gyZIH1LUrs"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/5gyZIH1LUrs/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCusTyoT4PeWxWgDRB_qMIIYwrmYg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/5gyZIH1LUrs"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/xZIt2ejiv78"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/xZIt2ejiv78/oardefault.jpg?sqp=-oaymwEoCJYDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB2umItw-akPlQTXzzw1x25ggmGDA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/xZIt2ejiv78"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Gg6dMpBb4Ng"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Gg6dMpBb4Ng/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB9RkIDXbUH3rdafB4wdgW-3VGXAA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Gg6dMpBb4Ng"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,6&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/FPCzcuRkVuQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/FPCzcuRkVuQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBInwJEohs-pun7Arr8ctOBzn7h0Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/FPCzcuRkVuQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/f0jhViwseZY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/f0jhViwseZY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCTRDf2d8RaMbfnGmq5f8kLsnRBzg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/f0jhViwseZY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,4&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Pf4aDtgVX-8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Pf4aDtgVX-8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAOrcqQvxllFPkS6YjWkAZKgNdnGw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Pf4aDtgVX-8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/eTdvvg03uPU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/eTdvvg03uPU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCSOWQCSVnrSbjwfc6LHa2jUhiNDg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/eTdvvg03uPU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/oPJPNzcCv_k"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/oPJPNzcCv_k/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAdu2BeqTt1wRPhD4jbnE131plc-Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/oPJPNzcCv_k"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Ankle Breaker King 😱 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Ankle Breaker King 😱 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/K_w3kh1yc48"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/K_w3kh1yc48/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAWIzZA3F3zsc01Lx5z341PvdS0NQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/K_w3kh1yc48"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,5&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/i1FSAqKR414"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/i1FSAqKR414/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAv-OnQZvpqEQBCuHKwEGxePdAt3Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/i1FSAqKR414"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,3&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/aTkmGlEy0gk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/aTkmGlEy0gk/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCceC9HPmrf7wkhuNUNB8GIqqZSCw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/aTkmGlEy0gk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/zGn50PiG_Zg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/zGn50PiG_Zg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDoJCq1MRAYpQkH83GKJLWKaQ_cpg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/zGn50PiG_Zg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="This Slap Turned Him SUS (@Power Slap) #shorts"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">This Slap Turned Him SUS (@Power Slap) #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AqAysxYNwjI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AqAysxYNwjI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC1c3fNOqwy2wyZaD72hF9_3aUAjg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AqAysxYNwjI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,2&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/bIGniOvpQ3w"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/bIGniOvpQ3w/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLANMBsqmCw06qc1bysraNpABfZ_fg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/bIGniOvpQ3w"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/0HpbLTThPQw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/0HpbLTThPQw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC-Xx-ARIumSk0FFXVAdb0nbtjkxA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/0HpbLTThPQw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">998&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/wY-L12z3vQA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/wY-L12z3vQA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBvFijW4yGBp2fMTmeSTxTL_pRPow">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/wY-L12z3vQA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/qqrKNa5TeAQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/qqrKNa5TeAQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDMmDajMKwkApZ5doPLSOhJGuBtzQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/qqrKNa5TeAQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pereira Gets Slapped HARD! (@alexpoatanpereira) #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pereira Gets Slapped HARD! (@alexpoatanpereira) #shorts</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1,1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/-i3_Qz0Yajo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/-i3_Qz0Yajo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDgYCTYREnW6JEaXiQYXEcBBKIJ4Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/-i3_Qz0Yajo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Ojto0Irg0Nc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Ojto0Irg0Nc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLALZpAyMXbkorWNOA7KnAh0Q2KozQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Ojto0Irg0Nc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1&nbsp;M de visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/zmKgF9P3O8M"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/zmKgF9P3O8M/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAQL3jRwweOiB6cYCqdFj2hS40wBw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/zmKgF9P3O8M"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">929&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/21zSK70ec9U"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/21zSK70ec9U/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB248XmVLjaS1zctYiS2DE0vE0RoA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/21zSK70ec9U"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">977&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/K9hfucI-YHw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/K9hfucI-YHw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAaE6PoE_2nVF-g8VsrpSbnVVDVMA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/K9hfucI-YHw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">920&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PXjdiTT4FVw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PXjdiTT4FVw/oardefault.jpg?sqp=-oaymwEoCIgDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDNphYINBXGw299wxvXzxVUE4cnyw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PXjdiTT4FVw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">963&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/6jfipoOaJsg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/6jfipoOaJsg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLASrOYwrBoo0Twyr3cHJouW04zS1w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/6jfipoOaJsg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">788&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/h1VyYpY7aB4"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/h1VyYpY7aB4/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAYN-5B96e0w5Jqj7Pg0cAkv4FGSA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/h1VyYpY7aB4"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">905&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Pr5xQSH5isk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Pr5xQSH5isk/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB3XLKTwN3RjIaKo8Loelj12hcbEg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Pr5xQSH5isk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="She Messed With the Wrong DJ 😎🔥 #shorts"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">She Messed With the Wrong DJ 😎🔥 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">758&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/sc9zJWEOLH8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/sc9zJWEOLH8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDx2HICAwNmNw5yTbfWrgLim6493A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/sc9zJWEOLH8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">907&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/YwBfj07x1b4"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/YwBfj07x1b4/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCKpML-GwnQPA2iRA4SXGun-BcGXw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/YwBfj07x1b4"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">779&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/hV3SymIvK-k"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/hV3SymIvK-k/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD_3XymFmzr3T-DmEw72P2IbMWVQw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/hV3SymIvK-k"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">884&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/EuUDuYNsoBU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/EuUDuYNsoBU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCjI-ZYo0NCKESSIEOLLUACVbnBqg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/EuUDuYNsoBU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">852&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/rVgcxRSD838"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/rVgcxRSD838/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCYfooB6EZsDm9mHK549_wkGK_tNg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/rVgcxRSD838"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Her First Basketball Shot 🥹(@zeelandschools)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Her First Basketball Shot 🥹(@zeelandschools)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">420&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/QZD9mJIfFow"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/QZD9mJIfFow"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">822&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/wBOsOVHKPRw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/wBOsOVHKPRw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="This Coach is a Sigma 🗿 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">This Coach is a Sigma 🗿 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">786&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/JdXmVanJChs"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/JdXmVanJChs"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">740&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/54rzYjGoXSo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/54rzYjGoXSo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">767&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/N4fDRr2-LaQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/N4fDRr2-LaQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">748&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/OPuhz-Tod3k"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/OPuhz-Tod3k"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="He Got Fired for Being a Human (@bryanjohnston_)"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He Got Fired for Being a Human (@bryanjohnston_)</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">642&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/m1GxFzDa3qM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/m1GxFzDa3qM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">729&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/f8lLyTl6Hlk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/f8lLyTl6Hlk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">714&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AcpvOvG_G8Q"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AcpvOvG_G8Q"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="#jaidmeel" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">#jaidmeel</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">631&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/z3To217vqEQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/z3To217vqEQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Last Kid Got Wrecked 💀 #shorts" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Last Kid Got Wrecked 💀 #shorts</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">689&nbsp;K visualizaciones</span></div>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="Más acciones">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer></div>"""  # aquí pegas el HTML
base_url = "https://www.youtube.com"

soup = BeautifulSoup(html, "html.parser")

short_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.startswith("/shorts/"):
        full_url = base_url + href
        if full_url not in short_links:
            short_links.append(full_url)

# Guardar en un archivo txt
save_links_to_txt(short_links, "shorts_links.txt")

print("✅ Links guardados en shorts_links.txt")
